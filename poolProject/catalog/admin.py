from django.contrib import admin
from .models import ServicesModel


@admin.register(ServicesModel)
class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_filter = ('title', 'subtitle')