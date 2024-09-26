from django.contrib import admin
from .models import ThemeBlogModel, BlogModel

@admin.register(ThemeBlogModel)
class ThemeBlogModelAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    search_fields = ('theme',)
    list_filter =('theme',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'publish', 'author')
    search_fields = ('title', 'pub_date', 'theme', 'author')
    list_filter = ('title', 'pub_date', 'theme', 'publish', 'author')
    prepopulated_fields = {"slug": ("title",)}