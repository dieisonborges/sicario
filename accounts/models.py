from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from .utils import rand_gen, path_and_rename

# Create your models here.

class UserProfile(models.Model):
    photo = models.ImageField('Foto', upload_to=path_and_rename, null=True)
    phone = models.CharField('Celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='profile')

    class Meta:
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'

    #For DjangoAdmin
    def __str__(self):
        return self.user.username