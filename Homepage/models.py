from django.db import models

# Create your models here.


class Destination(models.Model):

    no_of_dests = models.IntegerField()
    name = models.TextField(max_length=35)
    img = models.ImageField(upload_to='pics')
    path = models.TextField(max_length=200)