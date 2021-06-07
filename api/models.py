from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=1200)
    author=models.CharField(max_length=20)
    publisher=models.CharField(max_length=50)
    price=models.IntegerField()
    status=models.CharField(max_length=15)

    def __str__(self):
        return self.publisher
