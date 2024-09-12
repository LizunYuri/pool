from django.contrib import admin
from .models import ReviewModel


@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'sity', 'date', 'publish')
    search_fields = ('name', 'date', 'sity')
    list_filter = ('name', 'date', 'sity')
