from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_added"]
