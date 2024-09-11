from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('servises/<int:pk>/', views.service_detail, name='service_detail'),
    path('abouts/<int:pk>/', views.about_detail, name='about_detail'),
    path('catalog/category_detail/<slug:slug>', views.category_detail, name='category_detail')
]
