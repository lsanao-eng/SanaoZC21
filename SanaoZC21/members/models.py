from django.db import models

class member(models.Model):
  firstname = models.Charfield(max_length=255)
  lastname = models.Charfield(max_length=255)
# Create your models here.
