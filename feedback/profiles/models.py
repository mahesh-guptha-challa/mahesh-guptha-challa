from django.db import models

# Create your models here.


class UserProfile(models.Model):

    image_file = models.ImageField(upload_to="images")

