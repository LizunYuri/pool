import os
from django.db import models
from django.utils import timezone


class ReviewModel(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Имя клиента',
                            help_text='ФИО с согласия клиента')
    text = models.CharField(max_length=100,
                            verbose_name='Текст отзыва',
                            help_text='Со слов клиента, не болшьше 1000 символов')
    date = models.DateField(default=timezone.now,
                            verbose_name='Дата публикации')
    sity = models.CharField(max_length=200,
                            verbose_name='Город',
                            help_text='Город где построен объект')
    publish = models.BooleanField(verbose_name='Опубликовано',
                                  help_text='Добавляет отзыв на сайт', 
                                  default=False)
    image = models.ImageField(upload_to='review/',
                              verbose_name='Фото объекта',
                              help_text='Фото объекта')
    def __str__(self):

        return self.name

    
    def delete(self, *args, **kwargs):
        # Удаление файла изображения
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
      
    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural = 'Отзывы клиентов'