# Generated by Django 3.2 on 2024-09-06 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20240906_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firstpageaboutmodel',
            options={'verbose_name': 'Контент блока "о нас"', 'verbose_name_plural': 'Управление блоком "о нас"'},
        ),
        migrations.AddField(
            model_name='firstpageaboutmodel',
            name='icon',
            field=models.ImageField(default=django.utils.timezone.now, help_text='Использовать без фона', upload_to='content/icons', verbose_name='Иконка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='firstpageaboutmodel',
            name='subtitle',
            field=models.CharField(help_text='не больше 500, включая пробелы и знаки припенания', max_length=500, verbose_name='Подзаголовок блока "О нас"'),
        ),
        migrations.AlterField(
            model_name='firstpageaboutmodel',
            name='title',
            field=models.CharField(help_text='не больше 100 символов, включая пробелы и знаки припенания', max_length=100, verbose_name='Заголовок пункта "О нас"'),
        ),
    ]
