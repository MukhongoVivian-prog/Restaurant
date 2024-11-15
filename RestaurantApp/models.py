from django.db import models

from RestaurantApp.views import booking

# Create your models here.
class BookTable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    people =models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


