from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title
