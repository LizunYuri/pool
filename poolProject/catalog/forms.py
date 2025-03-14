import json
from django import forms
from django.contrib import admin
from .models import ServicesModel, ShopCategoryModel, ShopElementModel

class ServicesModelForm(forms.ModelForm):
    # Определяем поле как TextArea, чтобы ввести шаги вручную было удобнее
    methodology = forms.CharField(widget=forms.Textarea, help_text="Введите шаги в формате JSON")

    class Meta:
        model = ServicesModel
        fields = '__all__'

    def clean_steps(self):
        steps_data = self.cleaned_data['methodology']
        try:
            # Проверяем, что введенные данные — это корректный JSON
            steps_json = json.loads(steps_data)
            if not isinstance(steps_json, list):
                raise forms.ValidationError("Шаги должны быть списком объектов.")
        except ValueError:
            raise forms.ValidationError("Неправильный формат JSON.")
        
        return steps_data

@admin.register(ServicesModel)
class ServicesAdmin(admin.ModelAdmin):
    form = ServicesModel




# class TypeProductForm(forms.ModelForm):
#     class Meta:
#         model = ShopCategoryModel
#         fields = ['type']
#         widgets = {
#             'type': forms.Select(attrs={'class': 'form-control'}),
#         }

# # Форма для ввода категории товара
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = ShopCategoryModel
#         fields = ['category']
#         widgets = {
#             'category': forms.TextInput(attrs={'class': 'form-control'}),
#         }
