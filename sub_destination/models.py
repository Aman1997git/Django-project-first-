from django.db import models

# Create your models here.


class IndiaDestionation(models.Model):

    price = models.IntegerField()
    name = models.TextField(max_length=35)
    img = models.ImageField(upload_to='pics')
    review = models.IntegerField()
    duration = models.IntegerField()
    desc = models.TextField(max_length=35)


class ChinaDestionation(models.Model):

    price = models.IntegerField()
    name = models.TextField(max_length=35)
    img = models.ImageField(upload_to='pics')
    review = models.IntegerField()
    duration = models.IntegerField()
    desc = models.TextField(max_length=35)


class JapanDestionation(models.Model):

    price = models.IntegerField()
    name = models.TextField(max_length=35)
    img = models.ImageField(upload_to='pics')
    review = models.IntegerField()
    duration = models.IntegerField()
    desc = models.TextField(max_length=35)


class NepalDestionation(models.Model):

    price = models.IntegerField()
    name = models.TextField(max_length=35)
    img = models.ImageField(upload_to='pics')
    review = models.IntegerField()
    duration = models.IntegerField()
    desc = models.TextField(max_length=35)


class IndonasiaDestionation(models.Model):

    price = models.IntegerField()
    name = models.TextField(max_length=35)
    img = models.ImageField(upload_to='pics')
    review = models.IntegerField()
    duration = models.IntegerField()
    desc = models.TextField(max_length=35)


class ThailandDestionation(models.Model):

    price = models.IntegerField()
    name = models.TextField(max_length=35)
    img = models.ImageField(upload_to='pics')
    review = models.IntegerField()
    duration = models.IntegerField()
    desc = models.TextField(max_length=35)
