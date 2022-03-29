from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish_datetime = models.DateTimeField(default=timezone.now)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_update_datetime = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
