from django.contrib import admin
from .models import PersonalModel, SertificatesModel

@admin.register(PersonalModel)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title')
    search_fields = ('name', 'job_title')
    list_filter = ('name', 'job_title')


@admin.register(SertificatesModel)
class SertificateModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'year')
    search_fields = ('title', 'company', 'year')
    list_filter = ('title', 'company', 'year')