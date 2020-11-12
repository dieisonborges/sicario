from django.conf import settings
from django.db import models
from django.utils import timezone
import filetype
from django.contrib.auth.models import User, Group

from .utils import random_protocol_generate, path_and_rename

from teams.models import Team

# Create your models here.


class Ticket(models.Model):
    """ Ticket are called """
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ticket')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    teams = models.ManyToManyField(Team, related_name='tickets')
    protocol = models.CharField(max_length=10, unique=True)
    status = models.BooleanField('Status', default=False)#False=Close True=Open
    short_description = models.CharField('Título', max_length=50)
    description = models.TextField('Descrição')
    docfile = models.FileField('Arquivo', upload_to=path_and_rename, null=True)
    deadline = models.DateTimeField('Prazo', null=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ['id']
    
    def DocFileType(self):
        return filetype.guess(self.docfile.path)
    
    def DocFileTypeGroup(self):
        group = filetype.guess(self.docfile.path).mime
        group = group.split("/")
        return group[0]

    #For DjangoAdmin
    def __str__(self):
        return self.short_description

class Action(models.Model):
    """ Ticket Action """
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name = "actions")
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')
    short_description = models.CharField('Título',max_length=50)
    description = models.TextField('Descrição')
    docfile = models.FileField('Arquivo', upload_to=path_and_rename, null=True)
    time = models.IntegerField('Tempo Utilizado', default=0) #time used in the task in minutes
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"
        ordering = ['id']
    
    def DocFileType(self):
        return filetype.guess(self.docfile.path)
    
    def DocFileTypeGroup(self):
        group = filetype.guess(self.docfile.path).mime
        group = group.split("/")
        return group[0]
    
    #For DjangoAdmin
    def __str__(self):
        return self.short_description
