# myapp/admin.py
from django.contrib import admin
from .models import FirstPageTitleModel

@admin.register(FirstPageTitleModel)
class FirstPageTitleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'welcome')
    search_fields = ('title', 'subtitle')
    list_filter = ('title', 'subtitle')
