from autoslug import AutoSlugField
from django.db import models
from datetime import datetime

from django.conf import settings

from categories.models import Category
from .choices import condition_choices


class Ad(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name="seller",
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False,
                                 blank=False, on_delete=models.DO_NOTHING)
    condition = models.CharField(choices=condition_choices, max_length=10)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    phone = models.IntegerField()
    facebook = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='images/ads/images/ads/%Y/%m/%d/',
                                   default='ads/default.jpg', blank=True)
    photo_1 = models.ImageField(upload_to='images/ads/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='images/ads/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='images/ads/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='images/ads/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='images/ads/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='images/ads/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
