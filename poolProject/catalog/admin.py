from django.contrib import admin
from .models import ServicesModel, Photo, ShopCategoryModel, ShopElementModel, DiscountModel


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

@admin.register(DiscountModel)
class DiscountModelADmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'date_of', 'date_to')
    search_fields = ('title', 'date_of', 'date_to')
    list_filter = ('title', 'date_of', 'date_to')

@admin.register(Photo)
class PhotoADmin(admin.ModelAdmin):
    list_display = ('image',)