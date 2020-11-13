from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Equipment(models.Model):

    CHOICE_STATUS = (
        ('1', 'Operacional'),
        ('2', 'Inoperante Parcialmente'),
        ('3', 'Inoperante Total'),        
    )

    name = models.CharField('Nome', max_length=200)
    description = models.TextField('Descrição') 
    status = models.CharField('Situação', max_length=1, choices=CHOICE_STATUS, default=1)
    icon = models.CharField('Ícone', null=True, max_length=200)    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    #For DjangoAdmin
    def __str__(self):
        return self.name

class Connection(models.Model):
    description = models.CharField('Descrição', max_length=200)
    before = models.ForeignKey(
        Equipment,
            on_delete=models.CASCADE,
            related_name = "before",
            blank=True,
            null=True
        )
    after = models.ForeignKey(
        Equipment,
            on_delete=models.CASCADE,
            related_name = "after",
            blank=True,
            null=True
        ) 
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Conexão'
        verbose_name_plural = 'Conexões'

    #For DjangoAdmin
    def __str__(self):
        return self.description
