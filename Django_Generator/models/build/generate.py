from django.db import models
import os
os.environ.
class Step(models.Model):
    name = models.CharField(max_length=250, blank=False, null= False)

class Command(models.Model):

