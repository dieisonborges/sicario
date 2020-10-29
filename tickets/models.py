from django.conf import settings
from django.db import models

from .utils import random_protocol_generate

# Create your models here.

class Ticket(models.Model):
    """ Ticket are called """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    protocol = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=False)#False=Close True=Open
    short_description = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class Action(models.Model):
    """ Ticket Action """
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name = "actions")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

