from django.db import models

class Level(models.Model):
    no = models.IntegerField(default=0)
    text = models.CharField(max_length=1500, blank=True)
    picture = models.ImageField(upload_to='clues', default='', blank=True)
    hiddenHTML = models.CharField(max_length=1500, blank=True)
    answer = models.CharField(max_length=150)