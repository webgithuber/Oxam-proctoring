from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Model for Candidate Details
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    activation_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
#Model for Image Details
class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=False)
    activation_code = models.CharField(max_length=100)
    created_at = models.TimeField(null=True)
    
    def __str__(self):
        return self.email
