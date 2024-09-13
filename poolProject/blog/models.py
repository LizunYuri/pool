import os
from django.utils import timezone
from django.db import models


class ThemeBlogModel(models.Model):
    theme = models.CharField(max_length=200,
                             verbose_name='Тема',
                             help_text='Тематика блога')
    def __str__(self):
        return self.theme
    
    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы статей и бологов'

class BlogModel(models.Model):
    theme = models.ForeignKey(ThemeBlogModel,
                                    verbose_name='Тема статьи',
                                    help_text='Выберите одну тему', 
                                    on_delete=models.CASCADE)
    title = models.CharField(max_length=100,
                             verbose_name='Заголовок статьи',
                             help_text='Не больше 100 символов')
    subtitle = models.CharField(max_length=70,
                                verbose_name='Подзаголовок статьи',
                                help_text='Не больше 70 символов, не обязательно к заполнению',
                                null=True,
                                blank=True)
    pub_date = models.DateField(default=timezone.now,
                                verbose_name='Дата публикации',
                                help_text='Дата публикации')
    publish = models.BooleanField(verbose_name='Опубликовано',
                                  default=False,
                                  help_text='Отметка публикации на сайте')
    text = models.TextField(verbose_name='Текст статьи',
                            help_text='Полный текст статьи')
    img = models.ImageField(upload_to='blog/',
                            verbose_name='Обложка блога',
                            help_text='Красивое фото')
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name='URL')
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Удаление файла изображения
        if self.image and os.path.isfile(self.img.path):
            os.remove(self.img.path)
        super().delete(*args, **kwargs)

    def get_image_url(self):
        if self.img:
            return self.img.url
        return None
    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи и публикации компании'