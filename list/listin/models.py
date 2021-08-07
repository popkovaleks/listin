from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=SET_DEFAULT, default='')
    release_date = models.DateField()
    genre = models.ManyToManyField("Genre")
    language = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name