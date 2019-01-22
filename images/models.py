from django.db import models
# Create your models here.


class Set_1(models.Model):
    image_url = models.TextField(max_length=300, default='')

    def __str__(self):
        template = '{0.id}'
        return template.format(self)


class High_resolve_urls(models.Model):
    high_resolve_urls = models.TextField(max_length=300, default='')

    def __str__(self):
        template = '{0.id}'
        return template.format(self)
