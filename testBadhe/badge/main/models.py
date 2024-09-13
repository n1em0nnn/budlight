from django.db import models


class Title_news(models.Model):
    title_news = models.CharField('Название',max_length=100, default='News!')
    anons = models.CharField('Анонс',max_length=255, default='')
    full_text = models.TextField('Статья')
    dates = models.DateTimeField('Дата: ')

    def __str__(self):
        return self.title_news
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'