from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Place(models.Model):
  visitor = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
  visit = models.CharField(max_length=64)
  description =  models.TextField(default='Please Enter a Description')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.visit
