from django.db import models
from django.contrib.postgres.fields import ArrayField


class Person(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    aliases = ArrayField(models.CharField(max_length=256), null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=256)
    release_year = models.IntegerField()
    cast = models.ManyToManyField('Person', related_name='as_actor')
    directors = models.ManyToManyField('Person', related_name='as_director')
    producers = models.ManyToManyField('Person', related_name='as_producer')

    def __str__(self):
        return f"{self.title} ({self.release_year})"
