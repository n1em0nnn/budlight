from django.db import models

class Badge(models.Model):
    name = models.CharField('Название', max_length=50)
    desc = models.TextField('Описание')
    cost = models.IntegerField('Стоимость')

    def __str__(self):
        return self.name

