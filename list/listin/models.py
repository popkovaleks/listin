from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=SET_DEFAULT, default='')
    release_date = models.DateField(blank=True, null=True)
    genre = models.ManyToManyField("Genre", blank=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name