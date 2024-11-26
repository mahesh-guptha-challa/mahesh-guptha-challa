from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Feedback(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self) -> str:
        return f"{self.username} {self.description} {self.rating}"