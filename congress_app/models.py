from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  created_at = DateTimeField(auto_now_add=True, null=True)
  updated_at = DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name} {self.email}"
