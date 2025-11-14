from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    """Extended user model for housemates"""
    pass
# Create your models here.
class Events(models.Model):
    """Model representing Events"""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length= 1000)
    address = models.CharField(max_length=255)
    poster = models.ManyToManyField(User, related_name='posted by')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']
    
    