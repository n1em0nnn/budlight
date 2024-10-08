from django.db import models

class Badge(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField('Название', max_length=50)
    desc = models.TextField('Описание')
    cost = models.IntegerField('Стоимость')

    def __str__(self):
        return self.name



class BadgeToUser(models.Model):
    user_id=models.IntegerField('Код пользователя')
    badge_id= models.IntegerField('Код значка')