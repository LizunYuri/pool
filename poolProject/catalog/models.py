import os
from django.utils import timezone
from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _


class ServicesModel(models.Model):
    title = models.CharField( max_length=100,
                             help_text='Название',
                             verbose_name='Не больше 100 символов',
                             )
    
    subtitle = models.CharField( max_length=300,
                             help_text='Подзаголовок',
                             verbose_name='Краткое описание услуги, не больше 300 символов',
                             )
    
    includes = models.CharField( max_length=100,
                             help_text='Не больше 100 символов',
                             verbose_name='включает в себя')
    
    adouts = models.CharField( max_length=100,
                             help_text='Не больше 100 символов',
                             verbose_name='Об услуге')
    
    methodology = models.JSONField()
    
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
    
    def delete(self, *args, **kwargs):
        # Удаление файла изображения
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Услуги компании'
        verbose_name_plural = 'Услуги предоставляемые компанией'


class ShopCategoryModel(models.Model):

    class TypeProduct(models.IntegerChoices):
        POOL = 1, _('Бассейны')
        EQUIPMENT = 2, _('Оборудование')
        MATERIAL = 3, _('Материалы')

    ICONS = {
        TypeProduct.POOL: 'icons/pool.svg',
        TypeProduct.EQUIPMENT: 'icons/water-pump.svg',
        TypeProduct.MATERIAL: 'icons/material.svg',
    }

    type = models.IntegerField(choices=TypeProduct.choices, verbose_name='Тип категории')

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

    @property
    def icon(self):
        return self.ICONS.get(self.type)


class ShopElementModel(models.Model):

    date = models.DateField(default=timezone.now,
                            verbose_name='Дата публикации')
    
    category = models.ForeignKey(ShopCategoryModel, 
                                 verbose_name='Категория товара',
                                 help_text='Выбрать категорию', 
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=200, 
                             verbose_name='Название продукции',
                             help_text='Не больше 200 сиволов')
    length = models.FloatField(verbose_name='Длина',
                            help_text='Для чаши бассейна, если другая категория то не заполнять!',
                            default=0.00,
                            blank=True,
                            null=True)
    width = models.FloatField(verbose_name='Ширина',
                            help_text='Для чаши бассейна, если другая категория то не заполнять!',
                            default=0.00,
                            blank=True,
                            null=True)
    depth = models.FloatField(verbose_name='Глубина',
                            help_text='Для чаши бассейна, если другая категория то не заполнять!',
                            default=0.00,
                            blank=True,
                            null=True)
    description = models.TextField(verbose_name='Подробное описание продукции',
                                   help_text='Описать приемущества и недостатки, максимально подробно')
    price_to = models.FloatField(verbose_name='Цена от',
                                  default=0.00,
                                  help_text='Стоимость от. Не обязательно к заполнению',
                                  blank=True,
                                  null=True)
    image = models.ManyToManyField('Photo', 
                                   related_name='product',
                              verbose_name='Фото товара',
                              help_text='Красивое фото используется для оформления обложки страницы с описанием услуги')
    
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def save(self, *args, **kwargs):

        self.length = round(self.length, 2)
        self.width = round(self.width, 2)
        self.depth = round(self.depth, 2)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title
          
    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Каталог товаров'

class Photo(models.Model):
    image = models.ImageField(upload_to='catalog/product/',
                              verbose_name='Фото товара',
                              help_text='Красивое фото используется для оформления обложки страницы с описанием услуги')
    
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
        verbose_name='Изображение'
        verbose_name_plural = 'Загруженные изображения'

class DiscountModel(models.Model):
    title = models.CharField(max_length=70,
                             verbose_name='Заголовок',
                             help_text='Не больше 70 символов')
    description = models.CharField(max_length=100,
                                   verbose_name='Краткое описание',
                                   help_text='Не больше 100 символов')
    conditions = models.CharField(max_length=100,
                                  verbose_name='Спецпредложение',
                                  help_text='Не больше 100 символов',
                                  null=True)
    percent = models.IntegerField(verbose_name='Процент',
                                help_text='Если подразумевается скидка',
                                null=True,
                                blank=True)
    date_of = models.DateField(verbose_name='Дата начала',
                               help_text='Дата начала акции',
                               default=timezone.now)
    date_to = models.DateField(verbose_name='Дата окончания',
                               help_text='Дата окончания акции',
                               default=timezone.now)
    publish = models.BooleanField(default=True, verbose_name='Опубликовано')
    
    def save(self, *args, **kwargs):
        
        if self.date_to < date.today():
            self.publish = False
        super().save(*args, **kwargs)
    
    def __str__(self):

        return self.title
    
    class Meta:
        verbose_name = 'Спецпредложение'
        verbose_name_plural = 'Скидки и акции'

