# Generated by Django 3.2 on 2024-09-06 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicesmodel',
            options={'verbose_name': 'Услуги компаии', 'verbose_name_plural': 'Услуги предоставляемые компанией'},
        ),
        migrations.RemoveField(
            model_name='servicesmodel',
            name='slug',
        ),
    ]
