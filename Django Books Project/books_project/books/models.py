from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Address(models.Model):
    house_number = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null = True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class Book(models.Model):

    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=None)
    slug = models.SlugField(default="", null=False, db_index=True, unique=True)
    # models.CASCADE, models.SET_NULL, models.PROTECT, models.default
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, related_name="books")

    def path_of_the_url(self):  
        return reverse("model_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"


