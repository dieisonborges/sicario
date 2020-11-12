from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Equipaments(models.Model):

    name = models.CharField('Nome', max_length=200)
    description = models.TextField('Descrição') 
    icon = models.CharField('Ícone', null=True, max_length=200)    
    connections = models.ManyToManyField("app.Model", related_name='connections', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    #For DjangoAdmin
    def __str__(self):
        return self.name
