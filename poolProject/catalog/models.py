import os
from django.db import models


class ServicesModel(models.Model):
    title = models.CharField( max_length=100,
                             help_text='Название',
                             verbose_name='Не больше 100 символов',
                             )
    
    subtitle = models.CharField( max_length=300,
                             help_text='Подзаголовок',
                             verbose_name='Краткое описание услуги, не больше 300 символов',
                             )
    
    price_min = models.FloatField(verbose_name='Цена от',
                                  default=0.00,
                                  help_text='Стоимость от. Не обязательно к заполнению',
                                  blank=True,
                                  null=True)
    
    price_max = models.FloatField(verbose_name='Цена до',
                                  default=0.00,
                                  help_text='Стоимость до. Не обязательно к заполнению',
                                  blank=True,
                                  null=True)
    
    description = models.TextField(verbose_name='Описание',
                                   help_text='Подробное описание услуги')
    
    image = models.ImageField(upload_to='catalog/services/',
                              verbose_name='Обложка',
                              help_text='Красивое фото используется для оформления обложки страницы с описанием услуги')
    
    def __str__(self):

        return self.title
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
    
    def save(self, *args, **kwargs):

        self.price_min = round(self.price_min, 2)
        self.price_max = round(self.price_max, 2)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Удаление файла изображения
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Услуги компании'
        verbose_name_plural = 'Услуги предоставляемые компанией'


