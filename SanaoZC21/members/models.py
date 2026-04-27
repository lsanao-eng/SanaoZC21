from django.db import models

class members(models.Model):
  firstname = models.Charfield(max_length=255)
  lastname = models.Charfield(max_length=255)
# Create your models here.
