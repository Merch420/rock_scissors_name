from django.db import models

class User(models.Model):
    title = models.CharField('Username', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title