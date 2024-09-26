from django import forms
from .models import BlogModel, ThemeBlogModel
from company.models import PersonalModel


class BlogFilterForm(forms.Form):
    theme = forms.ModelChoiceField(queryset=ThemeBlogModel.objects.all(),
                                   required=False,
                                   label='Тема')
    author = forms.ModelChoiceField(queryset=PersonalModel.objects.all(),
                                    required=False,
                                    label='Автор')