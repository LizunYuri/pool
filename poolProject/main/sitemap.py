from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from blog.models import BlogModel
from catalog.models import ServicesModel, ShopCategoryModel, ShopElementModel
from blog.models import BlogModel

class StaticViewSitemap(Sitemap):
    changefreq = 'mounthly'
    priority = 0.5

    def items(self):
        return [
            'index',
            'services',
            'about',
            'blogs',
            'catalog',
            'contact',
            'nofound',
            'license',
            'cookie',
            'robots_txt'
            ]
    

    def location(self, item):

        return reverse(item)
    

class ServicesModelSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.6

    def items(self):
        return ServicesModel.objects.all()
    
    def location(self, item):
        return reverse('service_detail', args=[item.pk])


class ShopCategorySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return ShopCategoryModel.objects.all()
    
    def location(self, item):
        return reverse('category_detail', args=[item.slug])


class ShopElementSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return ShopElementModel.objects.all()
    
    def location(self, item):
        return reverse('product_detail', args=[item.slug])
    

class BlogModelSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return BlogModel.objects.all()
    
    def location(self, item):
        return reverse('blog_detail', args=[item.slug])