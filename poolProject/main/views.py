from django.shortcuts import render, get_object_or_404
from content.models import AboutValuesModel, FirstPageTitleModel, FirstPageAboutModel, FirstPageAwesomeModel
from catalog.models import ServicesModel, ShopCategoryModel, ShopElementModel, DiscountModel
from review.models import ReviewModel
from blog.models import BlogModel, ThemeBlogModel
from company.models import PersonalModel, SertificatesModel
from django.http import JsonResponse
from datetime import date
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from blog.form import BlogFilterForm


def index(request):
    titles = FirstPageTitleModel.objects.all()
    services = ServicesModel.objects.all()
    abouts = FirstPageAboutModel.objects.all()
    categories = ShopCategoryModel.objects.all()
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


def service_detail(request, pk):
    service = get_object_or_404(ServicesModel, pk=pk)

    return render(request, 'catalog/services_detail.html', {'service' : service})


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


def category_detail(request, slug):

    category = get_object_or_404(ShopCategoryModel, slug=slug)
    products = ShopElementModel.objects.filter(category=category)
    
    return render(request, 'catalog/category_detail.html', {'category': category, 'products': products})


def blogs(request):
    blogs = BlogModel.objects.all().order_by('-pub_date')
    paginator = Paginator(blogs, 3)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Истории", "url": 'blogs/'}
    ]

    # Передаем page_obj в шаблон
    return render(request, 'blog/blog.html', {
        'page_obj': page_obj,
        'breadcrumbs': breadcrumbs,
    })


def blog_list(request):
    blogs = BlogModel.objects.all().order_by('-pub_date')

    form = BlogFilterForm()

    paginator = Paginator(blogs, 3)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Если это AJAX запрос, возвращаем только HTML записей
    if request.is_ajax():
        html = render_to_string('blog/_blog_list_partial.html', {'page_obj': page_obj})

        return JsonResponse({
            'blogs': html,
            'has_next': page_obj.has_next()
        })
    


    # Для обычных запросов рендерим всю страницу
    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Истории", "url": 'blogs/'}
    ]

    return render(request, 'blog/blog.html', {
        'page_obj': page_obj,
        'form' : form,
        'breadcrumbs': breadcrumbs,
    })



def blog_detail(request, slug):
    blog = get_object_or_404(BlogModel, slug=slug)
    
    form = BlogFilterForm()

    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Истории", "url" : f"/blogs/"},
        {"name": blog.title, "url": request.path},
    ]

    return render(request, 'blog/blog_detail.html', {'blog' : blog,
                                                     'breadcrumbs' : breadcrumbs})


def catalog(request):
    
    return render(request, 'catalog/catalog.html')