from django.db import models
from datetime import datetime
import django
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=500)

class Post(models.Model):

    title = models.CharField(max_length=500)
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=500)
    date = models.DateField(default=django.utils.timezone.now)
    slug = models.CharField(max_length=500, unique=True)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="author")   
    tag = models.ManyToManyField(Tag, related_name="tag")


class Author(models.Model):

    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
