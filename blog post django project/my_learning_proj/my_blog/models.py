from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Books(models.Model):

    title = models.CharField(max_length=25)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    author = models.CharField(max_length=100,null=True)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} {self.rating}"
    