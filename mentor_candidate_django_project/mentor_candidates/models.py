from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mentor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name


class Opinion(models.Model):
    mentor = models.ForeignKey(Mentor)
    name = models.CharField(max_length=300)
    description = models.TextField()
    def __str__(self):
        return self.name
