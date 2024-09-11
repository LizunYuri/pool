from django.shortcuts import render, get_object_or_404
from content.models import FirstPageTitleModel, FirstPageAboutModel
from catalog.models import ServicesModel, ShopCategoryModel, ShopElementModel
from django.http import JsonResponse



def index(request):
    titles = FirstPageTitleModel.objects.all()
    services = ServicesModel.objects.all()
    abouts = FirstPageAboutModel.objects.all()
    categories = ShopCategoryModel.objects.all()

    categories_with_products = []

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
                                               })



def service_detail(request, pk):
    service = get_object_or_404(ServicesModel, pk=pk)

    return render(request, 'catalog/services_detail.html', {'service' : service})





def about_detail(request, pk):
    
    about_detail = get_object_or_404(FirstPageAboutModel, pk=pk)

    return render(request, 'components/about_detail.html', {'about_detail': about_detail})


def category_detail(request, slug):

    category = get_object_or_404(ShopCategoryModel, slug=slug)
    products = ShopElementModel.objects.filter(category=category)
    
    return render(request, 'catalog/category_detail.html', {'category': category, 'products': products})