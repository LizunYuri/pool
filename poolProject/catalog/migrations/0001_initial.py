# Generated by Django 3.2 on 2024-09-12 11:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название', max_length=100, verbose_name='Не больше 100 символов')),
                ('subtitle', models.CharField(help_text='Подзаголовок', max_length=300, verbose_name='Краткое описание услуги, не больше 300 символов')),
                ('price_min', models.FloatField(blank=True, default=0.0, help_text='Стоимость от. Не обязательно к заполнению', null=True, verbose_name='Цена от')),
                ('price_max', models.FloatField(blank=True, default=0.0, help_text='Стоимость до. Не обязательно к заполнению', null=True, verbose_name='Цена до')),
                ('description', models.TextField(help_text='Подробное описание услуги', verbose_name='Описание')),
                ('image', models.ImageField(help_text='Красивое фото используется для оформления обложки страницы с описанием услуги', upload_to='catalog/services/', verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'Услуги компании',
                'verbose_name_plural': 'Услуги предоставляемые компанией',
            },
        ),
        migrations.CreateModel(
            name='ShopCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(help_text='Указать категорию товаров', max_length=200, verbose_name='Категория товара')),
                ('image', models.ImageField(help_text='Красивое фото используется для оформления обложки страницы с описанием услуги', upload_to='catalog/cover/', verbose_name='Фото для обложки группы')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории товаров',
                'verbose_name_plural': 'Категория товара',
            },
        ),
        migrations.CreateModel(
            name='ShopElementModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('title', models.CharField(help_text='Не больше 200 сиволов', max_length=200, verbose_name='Название продукции')),
                ('dimensions', models.CharField(help_text='Введите в формате ДДxШШxГГ', max_length=20, verbose_name='Размер бассейна')),
                ('description', models.TextField(help_text='Описать приемущества и недостатки, максимально подробно', verbose_name='Подробное описание продукции')),
                ('price_to', models.FloatField(blank=True, default=0.0, help_text='Стоимость от. Не обязательно к заполнению', null=True, verbose_name='Цена от')),
                ('image', models.ImageField(help_text='Красивое фото используется для оформления обложки страницы с описанием услуги', upload_to='catalog/product/', verbose_name='Фото товара')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(help_text='Выбрать категорию', on_delete=django.db.models.deletion.CASCADE, to='catalog.shopcategorymodel', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Каталог товаров',
            },
        ),
    ]
