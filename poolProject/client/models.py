from django.db import models

class SiteClientModel(models.Model):
    name  = models.CharField(max_length=100,
                            verbose_name='Фамилия и Имя')
    phone = models.CharField(max_length=100,
                            verbose_name='Номер телефона')
    city = models.CharField(max_length=100,
                            verbose_name='Город')
    def __str__(self):

        return self.name
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'База клиентов'