from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    """ Team are called """
    user = models.ManyToManyField(User, related_name='teams')
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"
        ordering = ['id']

    #For DjangoAdmin
    def __str__(self):
        return self.name