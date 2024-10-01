from django.urls import path
from django.shortcuts import render
from django.conf.urls import handler404
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemap import BlogModelSitemap, ShopElementSitemap, StaticViewSitemap, ServicesModelSitemap, ShopCategorySitemap


sitemaps = {
    'static' : StaticViewSitemap(),
    'services' : ServicesModelSitemap(),
    'catalog_category' : ShopCategorySitemap(),
    'product_detail' : ShopElementSitemap(),
    'blogs' : BlogModelSitemap(),
    }


urlpatterns = [
    path('save-form-data/', views.save_form_data, name='save_form_data'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('about/', views.about, name='about'),
    path('abouts/<int:pk>/', views.about_detail, name='about_detail'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/records/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('catalog/product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('catalog/filter/', views.filter_catalog, name='filter_catalog'),
    path('contact/', views.contact, name='contact'),
    path('cookie/', views.cookie, name='cookie'),
    path('info/', views.info, name='info'),
    path('license/', views.license, name='license'),
    path('nofound/', views.nofound, name='nofound'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]


def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)

# Укажите обработчик для 404 ошибок
handler404 = 'main.urls.custom_404_view'