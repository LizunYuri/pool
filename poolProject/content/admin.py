# myapp/admin.py
from django.contrib import admin
from .models import FirstPageTitleModel, FirstPageAboutModel

@admin.register(FirstPageTitleModel)
class FirstPageTitleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'welcome')
    search_fields = ('title', 'subtitle')
    list_filter = ('title', 'subtitle')


@admin.register(FirstPageAboutModel)
class FirstPageAboutModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')

    def has_add_permission(self, request):
        # Отключаем возможность создания записи, если существует 3 записи
        return FirstPageAboutModel.objects.count() < 3

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Сортируем по ID, если необходимо
        return queryset.order_by('id')
