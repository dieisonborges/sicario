from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

from .utils import rand_gen, path_and_rename

# Create your models here.

class UserProfile(models.Model):

    CHOICE_MILITARY_DESIGNATION = (
        ('Mar Ar', 'Marechal do Ar'),
        ('Ten Brig', 'Tenente-Brigadeiro'),
        ('Maj Brig', 'Major-Brigadeiro'),
        ('Brig', 'Brigadeiro'),
        ('Cel', 'Coronel'),
        ('Ten Cel', 'Tenente-Coronel'),
        ('Maj', 'Major'),
        ('Cap', 'Capitão'),
        ('1º Ten', '1º Tenente'),
        ('2º Ten', '2º Tenente'),
        ('Asp', 'Aspirante a Oficial'),
        ('Cad', 'Cadete'),
        ('SO', 'Suboficial'),
        ('1S', '1º Sargento'),
        ('2S', '2º Sargento'),
        ('3S', '3º Sargento'),
        ('Al', 'Aluno'),
        ('CB', 'Cabo'),
        ('TM', 'Taifero-mor'),
        ('S1', 'Soldado 1ª Classe'),
        ('T1', 'Taifeiro 1ª Classe'),
        ('S2', 'Soldado 2ª Classe'),
        ('T2', 'Taifeiro 2ª Classe'),
        ('CV', 'Civil'),
        ('Nenhum', 'Nenhum'),
    )

    photo = models.ImageField('Foto', upload_to=path_and_rename, null=True)
    phone = models.CharField('Celular', max_length=16)    
    individual_registration = models.CharField('CPF - Cadastro de Pessoa Física', max_length=11, blank=True)
    military_designation = models.CharField('Posto/Graduação', max_length=15, choices=CHOICE_MILITARY_DESIGNATION, blank=True)
    military_group = models.CharField('Quadro (Abreviação)', max_length=16, blank=True)
    military_specialty = models.CharField('Especialidade (Abreviação)', max_length=17, blank=True)
    military_war_name = models.CharField('Nome de Guerra', max_length=50, blank=True)
    military_health_number = models.CharField('SARAM', max_length=7, blank=True)
    military_validity_health_inspection = models.DateField('Validade da INSPSAU', default=datetime.now)
    military_last_health_inspection = models.DateField('Data da Última da INSPSAU', default=datetime.now)
    military_id = models.CharField('Identidade Funcional', max_length=6, blank=True)
    military_technical_qualification_certificate = models.CharField('Certificado de Habilitação Técnica - CHT', max_length=6, blank=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='profile')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'

    #For DjangoAdmin
    def __str__(self):
        return self.user.username

    #Check one profile for DjangoAdmin
    """
    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise ValidationError("Você já tem um perfil cadastrado.")
    """