from django.contrib import admin
from .models import PersonalModel

@admin.register(PersonalModel)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title')
    search_fields = ('name', 'job_title')
    list_filter = ('name', 'job_title')
