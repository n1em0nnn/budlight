from django.db import models
from django.forms import CharField


class CompModel(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    org = models.CharField(max_length=250)
    fcdo = models.BooleanField(default=False)
    result = models.CharField(max_length=10)
    def __str__(self):
        return self.name



class Result(models.Model):
    result_name = models.CharField(max_length=10)
    def __str__(self):
        return self.result_name

class CompLevel(models.Model):
    level_name = models.CharField(max_length=50)
    def __str__(self):
        return self.level_name