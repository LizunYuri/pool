from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('servises/<int:pk>/', views.service_detail, name='service_detail'),
    path('about/', views.about, name='about'),
    path('abouts/<int:pk>/', views.about_detail, name='about_detail'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog/records/<slug:slug>', views.blog_detail, name='blog_detail'),
    path('catalog/category_detail/<slug:slug>', views.category_detail, name='category_detail'),
    path('catalog/', views.catalog, name='catalog'),
]
