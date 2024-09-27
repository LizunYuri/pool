from django import forms
from .models import BlogModel, ThemeBlogModel
from company.models import PersonalModel


class BlogFilterForm(forms.Form):
    author = forms.ModelChoiceField(
        queryset=PersonalModel.objects.all(),
        required=False,
        label="Автор",
        empty_label="Все авторы"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['author'].queryset = PersonalModel.objects.all()

class BlogThemeFilter(forms.Form):
    theme = forms.ModelChoiceField(
        queryset=ThemeBlogModel.objects.all(),
        required=False,
        label='Тема',
        empty_label='Все темы'
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['theme'].queryset = ThemeBlogModel.objects.all()