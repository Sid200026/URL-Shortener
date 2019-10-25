from django.db import models
# Create your models here.

class url(models.Model):
    big_url = models.URLField(max_length=200)
    short_url = models.TextField(max_length=200, unique = True)

    def __str__(self):
        return self.short_url
    