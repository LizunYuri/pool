import os
from django.utils import timezone
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


class ShopCategoryModel(models.Model):
    category = models.CharField(max_length=200, 
                                verbose_name='Категория товара',
                                help_text='Указать категорию товаров')
    image = models.ImageField(upload_to='catalog/cover/',
                              verbose_name='Фото для обложки группы',
                              help_text='Красивое фото используется для оформления обложки страницы с описанием услуги')
    slug = models.SlugField(max_length=255, 
                            unique=True, 
                            db_index=True, 
                            verbose_name="URL")

    
    def __str__(self):
        return self.category
    
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
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категория товара'

class ShopElementModel(models.Model):
    date = models.DateField(default=timezone.now,
                            verbose_name='Дата публикации')
    category = models.ForeignKey(ShopCategoryModel, 
                                 verbose_name='Категория товара',
                                 help_text='Выбрать категорию', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, 
                             verbose_name='Название продукции',
                             help_text='Не больше 200 сиволов')
    dimensions = models.CharField(max_length=20,
                                  verbose_name='Размер бассейна', 
                                  help_text='Введите в формате ДДxШШxГГ')

    description = models.TextField(verbose_name='Подробное описание продукции',
                                   help_text='Описать приемущества и недостатки, максимально подробно')
    price_to = models.FloatField(verbose_name='Цена от',
                                  default=0.00,
                                  help_text='Стоимость от. Не обязательно к заполнению',
                                  blank=True,
                                  null=True)
    image = models.ImageField(upload_to='catalog/product/',
                              verbose_name='Фото товара',
                              help_text='Красивое фото используется для оформления обложки страницы с описанием услуги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def save(self, *args, **kwargs):

        self.price_to = round(self.price_to, 2)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title
    
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
        verbose_name='Товар'
        verbose_name_plural = 'Каталог товаров'