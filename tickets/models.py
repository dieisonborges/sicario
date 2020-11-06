from django.conf import settings
from django.db import models
from django.utils import timezone
import os
from uuid import uuid4

from .utils import random_protocol_generate, path_and_rename

# Create your models here.

class Ticket(models.Model):
    """ Ticket are called """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    protocol = models.CharField(max_length=10, unique=True)
    status = models.BooleanField('Status', default=False)#False=Close True=Open
    short_description = models.CharField('Título', max_length=50)
    description = models.TextField('Descrição')
    docfile = models.FileField(upload_to=path_and_rename)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ['id']
    
    #For DjangoAdmin
    def __str__(self):
        return self.short_description

class Action(models.Model):
    """ Ticket Action """
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name = "actions")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_description = models.CharField('Título',max_length=50)
    description = models.TextField('Descrição')
    docfile = models.FileField(upload_to=path_and_rename)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em',auto_now=True)

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"
        ordering = ['id']
    
    #For DjangoAdmin
    def __str__(self):
        return self.short_description
