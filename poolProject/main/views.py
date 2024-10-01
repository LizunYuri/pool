from django.shortcuts import render, get_object_or_404
from content.models import AboutValuesModel, FirstPageTitleModel, FirstPageAboutModel, FirstPageAwesomeModel
from catalog.models import ServicesModel, ShopCategoryModel, ShopElementModel, DiscountModel
from poolProject import settings
from review.models import ReviewModel
from blog.models import BlogModel, ThemeBlogModel
from company.models import PersonalModel, SertificatesModel
from django.http import HttpResponse, JsonResponse
from datetime import date
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from blog.form import BlogFilterForm, BlogThemeFilter
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from client.models import SiteClientModel
from django.core.mail import send_mail



def save_form_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        
        entry = SiteClientModel.objects.create(
                                        name=name,
                                        phone=phone,
                                        city=city)
        
        subject = f'Новая заявка от {name}'

            # Текст письма
        message = f'Имя: {name}\nГород: {city}\nТелефон: {phone}'
        recipient_list = ['recipient@example.com']

            # Отправка письма
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
            
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'fail'}, status=400)

def index(request):
    titles = FirstPageTitleModel.objects.all()
    services = ServicesModel.objects.all()
    abouts = FirstPageAboutModel.objects.all()
    categories = ShopCategoryModel.objects.all()[:3]
    reviews_publish = ReviewModel.objects.filter(publish=True)
    awesomes = FirstPageAwesomeModel.objects.all()
    discounts = DiscountModel.objects.filter(publish=True)
    blogs = BlogModel.objects.filter(publish=True)[:3]
    today = date.today()
    

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
    ]


    categories_with_products = []
    
    for discount in discounts:
        
        discount.days_left = (discount.date_to - today).days

    for category in categories:
        products = ShopElementModel.objects.filter(category=category)[:3]
        if products.exists():
            categories_with_products.append({
                'category' : category,
                'products' : products})
            
    return render(request, 'main/index.html', {'titles' : titles,
                                               'services' : services,
                                               'abouts' : abouts,
                                               'categories_with_products' : categories_with_products,
                                               'reviews': reviews_publish,
                                               'awesomes': awesomes,
                                               'discounts' : discounts,
                                               'blogs' : blogs,
                                               'breadcrumbs': breadcrumbs,
                                               })


def services(request):
    services = ServicesModel.objects.all()

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Услуги", "url": 'services/'}
    ]

    return render(request, 'services/services.html', {'services' : services,
                                                      'breadcrumbs' : breadcrumbs})


def service_detail(request, pk):

    service = get_object_or_404(ServicesModel, pk=pk)

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Услуги", "url" : f"/services/"},
        {"name": service.title, "url": request.path},
    ]

    return render(request, 'services/services_detail.html', {'service' : service,
                                                             'breadcrumbs' : breadcrumbs})


def about(request):
    values = AboutValuesModel.objects.all()
    personal = PersonalModel.objects.all()
    sertificates = SertificatesModel.objects.all()

    sertificates_exist = sertificates.exists()  # Проверяем наличие записей

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "О нас", "url": 'about/'}
    ]

    return render(request, 'main/about.html', {
        'values': values,
        'personal': personal,
        'breadcrumbs': breadcrumbs,
        'sertificates': sertificates,
        'sertificates_exist': sertificates_exist  # Передаем в шаблон
    })


def about_detail(request, pk):
    
    about_detail = get_object_or_404(FirstPageAboutModel, pk=pk)

    return render(request, 'components/about_detail.html', {'about_detail': about_detail})


def blogs(request):
    
    authors = PersonalModel.objects.all()
    theme =ThemeBlogModel.objects.all()

    sort = request.GET.get('sort', 'desc')
    author_id = request.GET.get('author')
    theme_id = request.GET.get('theme')

    # Получаем базовый QuerySet блогов
    blogs = BlogModel.objects.all()

    # Если выбран автор, фильтруем по автору
    if author_id:
        blogs = blogs.filter(author_id=author_id)

    if theme_id:
        blogs = blogs.filter(theme_id=theme_id)

    # Применяем сортировку
    if sort == 'asc':
        blogs = blogs.order_by('pub_date')
    else:
        blogs = blogs.order_by('-pub_date')

    paginator = Paginator(blogs, 3)  # Пагинация по 3 записи
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.is_ajax():
        html = render_to_string('blog/_blog_list_partial.html', {'page_obj': page_obj})
        return JsonResponse({
            'blogs': html,
            'has_next': page_obj.has_next()
        })

    form = BlogFilterForm()
    theme_form = BlogThemeFilter

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Истории", "url": 'blogs/'}
    ]


    return render(request, 'blog/blog.html', {
        'page_obj': page_obj,
        'form': form,
        'theme_form' : theme_form,
        'breadcrumbs': breadcrumbs,
    })


def blog_detail(request, slug):
    blog = get_object_or_404(BlogModel, slug=slug)
    
    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Истории", "url" : f"/blogs/"},
        {"name": blog.title, "url": request.path},
    ]

    return render(request, 'blog/blog_detail.html', {'blog' : blog,
                                                     'breadcrumbs' : breadcrumbs})


def catalog(request):
    categories = ShopCategoryModel.objects.all()

    categories_with_products = []

    # Получение уникальных типов категорий с их текстовыми представлениями
    unique_types = categories.values('type').distinct()

    # Получаем текстовые представления для каждого уникального типа
    unique_types_with_display = [
        {
            'type': type['type'],
            'display': ShopCategoryModel.TypeProduct(type['type']).label  # Получаем название из IntegerChoices
        }
        for type in unique_types
    ]

    # Фильтрация по типу и категории
    selected_type = request.GET.get('type', None)
    selected_category = request.GET.get('category', None)

    for category in categories:
        products = ShopElementModel.objects.filter(category=category)[:3]
        if products.exists():
            categories_with_products.append({
                'category': category,
                'products': products
            })

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Бассейны и оборудование", "url": 'catalog/'}
    ]

    return render(request, 'catalog/catalog.html', {
        'breadcrumbs': breadcrumbs,
        'categories': categories.distinct(),  # Уникальные категории
        'unique_types': unique_types_with_display,  # Передаем уникальные типы с названиями
        'categories_with_products': categories_with_products,
    })


def filter_catalog(request):
    selected_type = request.GET.get('type', None)
    selected_category = request.GET.get('category', None)

    # Получение всех категорий
    categories_with_products = []

    categories = ShopCategoryModel.objects.all()

    # Фильтрация по типу
    if selected_type:
        categories = categories.filter(type=selected_type)

    # Фильтрация по категории
    if selected_category:
        categories = categories.filter(id=selected_category)

    for category in categories:
        products = ShopElementModel.objects.filter(category=category)[:10]
        if products.exists():
            categories_with_products.append({
                'category': category,
                'products': products
            })

    return render(request, 'catalog/catalog_partial.html', {
        'categories_with_products': categories_with_products
    })


def category_detail(request, slug):
    category = get_object_or_404(ShopCategoryModel, slug=slug)

    sort_price = request.GET.get('sort_price', 'default')
    sort_length = request.GET.get('sort_length', 'default')
    products = ShopElementModel.objects.filter(category=category)

    # Сортировка по цене
    if sort_price == 'asc':
        products = products.order_by(F('price_to').asc(nulls_first=True))
    elif sort_price == 'desc':
        products = products.order_by(F('price_to').desc(nulls_first=True))

    # Сортировка по длине
    if sort_length == 'asc_length':
        products = products.order_by(F('length').asc(nulls_first=True), F('length').asc(nulls_first=True))  # Сначала пустые значения
    elif sort_length == 'desc_length':
        products = products.order_by(F('length').desc(nulls_first=True), F('length').asc(nulls_first=True))  # Сначала пустые значения

    # Если нет сортировки, по умолчанию
    if sort_price == 'default' and sort_length == 'default':
        products = products.order_by('-date')

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('catalog/_catalog_list_partial.html', {'page_obj': page_obj})
        return JsonResponse({
            'category': html,
            'has_next': page_obj.has_next()
        })

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Каталог", "url": "/catalog/"},
        {"name": category.category, "url": request.path},
    ]
    return render(request, 'catalog/category_detail.html', {
        'category': category,
        'page_obj': page_obj,
        'breadcrumbs': breadcrumbs
    })


def product_detail(request, slug):

    product = get_object_or_404(ShopElementModel, slug=slug)

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Каталог", "url" : f"/catalog/"},
         {"name": product.category, "url": f"/catalog/category/{product.category.slug}/"},
        {"name": product.title, "url": request.path},
    ]

    return render(request, 'catalog/product_detail.html', {'product' : product,
                                                           'breadcrumbs' : breadcrumbs})


def contact(request):
    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Контакты", "url" : f"/contact/"},
    ]

    return render(request, 'main/contact.html', {'breadcrumbs' : breadcrumbs})


def nofound(request):

    return render(request, 'errors/404.html')


def cookie(request):

    return render(request, 'errors/cookie.html')


def info(request):

    return render(request, 'errors/info.html')


def license(request):

    return render(request, 'errors/license.html')


def robots_txt(request):
    with open('robots.txt', 'r') as f:
        return HttpResponse(f.read(), content_type="text/plain")