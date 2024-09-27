from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


