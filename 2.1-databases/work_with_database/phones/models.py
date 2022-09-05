from django.db import models


class Phone(models.Model):

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL')
