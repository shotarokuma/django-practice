from django.db import models
from django.db.models.base import Model

# Create your models here.
class Items(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()

  class Meta:
    db_table = 'items'