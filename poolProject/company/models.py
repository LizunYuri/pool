import os
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class PersonalModel(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Фамилия и Имя',
                            help_text='На русском языке, не больше 100 символов')
    job_title = models.CharField(max_length=100,
                                 verbose_name='Должность',
                                 help_text='На русском языке, не больше 100 символов')
    quote = models.TextField(verbose_name='Текст',
                             help_text='Небольшое текстовое описание. напр. Стаж, профкссия и т.д, учитываются первые 20 слов')
    image = models.ImageField(upload_to='company/personal',
                              verbose_name='Обложка',
                              help_text='Портретное фото')
    
    def __str__(self):

        return self.name
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None

    def delete(self, *args, **kwargs):
        # Удаление файла изображения
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Персонал компании'


class SertificatesModel(models.Model):
    title = models.CharField(max_length=100,
                            verbose_name='Название сертификата',
                            help_text='На русском языке, не больше 100 символов')
    year = models.IntegerField(verbose_name='Год выдачи', 
                               validators= [
                                   MinValueValidator(1900), 
                                   MaxValueValidator(datetime.datetime.now().year)
                                   ],
                                   help_text='в формате ГГГГ')
    company = models.CharField(max_length=100,
                            verbose_name='Компания которая выдала сертификат',
                            help_text='На русском языке, не больше 100 символов')
    image = models.ImageField(upload_to='company/sertificates',
                              verbose_name='Обложка',
                              help_text='Портретное фото')
    
    def __str__(self):

        return self.title
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None

    def delete(self, *args, **kwargs):
        # Удаление файла изображения
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Дипломы и сертификаты персонала'