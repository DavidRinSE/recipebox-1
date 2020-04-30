from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField()
