# Generated by Django 3.2 on 2024-09-05 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FirstPageTitle',
            new_name='FirstPageTitleModel',
        ),
        migrations.AlterModelOptions(
            name='firstpagetitlemodel',
            options={'verbose_name': 'Редактирование контента', 'verbose_name_plural': 'Управление заголовками первой страницы'},
        ),
    ]
