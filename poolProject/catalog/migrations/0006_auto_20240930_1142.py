# Generated by Django 3.2 on 2024-09-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20240927_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcategorymodel',
            name='type',
            field=models.IntegerField(choices=[(1, 'Бассейны'), (2, 'Оборудование'), (3, 'Материалы')], default=1, verbose_name='Тип категории'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicesmodel',
            name='adouts',
            field=models.CharField(help_text='Не больше 100 символов', max_length=100, verbose_name='Об услуге'),
        ),
        migrations.AlterField(
            model_name='servicesmodel',
            name='includes',
            field=models.CharField(help_text='Не больше 100 символов', max_length=100, verbose_name='включает в себя'),
        ),
    ]
