# Generated by Django 3.2 on 2024-09-12 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='sity',
            field=models.CharField(default=django.utils.timezone.now, help_text='Город где построен объект', max_length=200, verbose_name='Город'),
            preserve_default=False,
        ),
    ]
