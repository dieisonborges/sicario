from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Equipment(models.Model):

    CHOICE_STATUS = (
        ('success', 'Operacional'),
        ('warning', 'Inoperante Parcialmente'),
        ('danger', 'Inoperante Total'),      
    )

    name = models.CharField('Nome', max_length=200)
    description = models.TextField('Descrição') 
    status = models.CharField('Situação', max_length=7, choices=CHOICE_STATUS, default=1)
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
    CHOICE_DIRECTION = (
        ('left', 'Recebe'),
        ('right', 'Envia'),
        ('exchange', 'Bi-direcional'),      
    )
    description = models.CharField('Descrição da Canalização', max_length=200)
    #equipments = models.ManyToManyField(Equipment, related_name='connections')
    equipment_left = models.ForeignKey(
        Equipment,
            on_delete=models.CASCADE,
            related_name = "equipment_left",
            verbose_name = "Equipamento",
            blank=True,
            null=True,
        )
    equipment_right = models.ForeignKey(
        Equipment,
            on_delete=models.CASCADE,
            related_name = "equipment_right",
            verbose_name = "Equipamento Conectado",
            blank=True,
            null=True,
        )  
    direction = models.CharField('Direção do Tráfego', max_length=8, choices=CHOICE_DIRECTION, default='left')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Conexão'
        verbose_name_plural = 'Conexões'

    #For DjangoAdmin
    def __str__(self):
        return self.description
