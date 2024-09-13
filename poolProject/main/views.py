from django.shortcuts import render, get_object_or_404
from content.models import AboutValuesModel, FirstPageTitleModel, FirstPageAboutModel, FirstPageAwesomeModel
from catalog.models import ServicesModel, ShopCategoryModel, ShopElementModel, DiscountModel
from review.models import ReviewModel
from blog.models import BlogModel
from company.models import PersonalModel
from django.http import JsonResponse
from datetime import date


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
    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name" : "О нас", "url" : 'about/'}
    ]

    return render(request, 'main/about.html', {'values' : values,
                                               'personal' : personal,
                                               'breadcrumbs': breadcrumbs,})


def about_detail(request, pk):
    
    about_detail = get_object_or_404(FirstPageAboutModel, pk=pk)

    return render(request, 'components/about_detail.html', {'about_detail': about_detail})




def category_detail(request, slug):

    category = get_object_or_404(ShopCategoryModel, slug=slug)
    products = ShopElementModel.objects.filter(category=category)
    
    return render(request, 'catalog/category_detail.html', {'category': category, 'products': products})

def blogs(request):
    breadcrumbs = [
        {"name": "Главная", "url": "/"},
        {"name": "Истории", "url" : 'blogs/'}
    ]
    return render(request, 'blog/blog.html', {'breadcrumbs' : breadcrumbs})

def blog_detail(request, slug):
    blog = get_object_or_404(BlogModel, slug=slug)

    return render(request, 'blog/blog_detail.html', {'blog' : blog})