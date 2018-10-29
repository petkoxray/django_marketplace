from autoslug import AutoSlugField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='photos/categories/', blank=False, null=False)

    def __str__(self):
        return self.name
