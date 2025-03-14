# Generated by Django 3.2 on 2024-09-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='На русском языке, не больше 100 символов', max_length=100, verbose_name='Фамилия и Имя')),
                ('job_title', models.CharField(help_text='На русском языке, не больше 100 символов', max_length=100, verbose_name='Должность')),
                ('quote', models.TextField(help_text='Небольшое текстовое описание. напр. Стаж, профкссия и т.д, учитываются первые 20 слов', verbose_name='Текст')),
                ('image', models.ImageField(help_text='Портретное фото', upload_to='company/personal', verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал компании',
            },
        ),
    ]
