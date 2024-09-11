from django.contrib import admin
from .models import ServicesModel, ShopCategoryModel, ShopElementModel


@admin.register(ServicesModel)
class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_filter = ('title', 'subtitle')



@admin.register(ShopCategoryModel)
class ShopCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category',)
    prepopulated_fields = {"slug": ("category",)}



@admin.register(ShopElementModel)
class ShopElementModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    search_fields = ('title', 'category', 'date')
    list_filter = ('title', 'category', 'date')
    prepopulated_fields = {"slug": ("title",)}