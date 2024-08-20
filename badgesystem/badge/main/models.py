from django.db import models


class Badges(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=200)
    cost = models.IntegerField('Стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бадж'
        verbose_name_plural= 'Баджи'

