from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mentor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    description = models.TextField()


class Opinion(models.Model):
    mentor = models.ForeignKey(Mentor)
    name = models.CharField(max_length=300)
    description = models.TextField()
