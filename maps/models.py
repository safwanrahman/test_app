from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pointer(models.Model):
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	address = models.TextField()