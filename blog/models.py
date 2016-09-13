from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=30)
    text=models.TextField()


class Comment(models.Model):
    user=models.CharField(max_length=15)
    comment=models.TextField()
