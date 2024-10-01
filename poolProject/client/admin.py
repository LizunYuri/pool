from django.contrib import admin
from .models import SiteClientModel

# Register your models here.
@admin.register(SiteClientModel)
class SiteClientModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone')
    search_fields = ('name', 'city', 'phone')
    list_filter = ('name', 'city', 'phone')
