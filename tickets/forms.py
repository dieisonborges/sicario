from django import forms
from django.contrib.auth.models import User, Group

from .utils import random_protocol_generate

from .models import Ticket, Action
from teams.models import Team

class TicketForm(forms.ModelForm):      
    docfile = forms.FileField(label='Anexo', required=False)
    #deadline = forms.CharField(label='Prazo', required=True)
    class Meta:
        model = Ticket
        fields = ('short_description', 'description', 'docfile', 'teams', 'deadline')
        #exclude = ()

class ActionForm(forms.ModelForm): 
    docfile = forms.FileField(label='Anexo', required=False)
    time = forms.IntegerField(label='Tempo utilizado em Minutos',  required=True)
    class Meta:
        model = Action        
        fields = ('short_description', 'description', 'docfile', 'time')        
        #exclude = ()

class TicketTeamForm(forms.ModelForm):      
    class Meta:
        model = Ticket
        fields = ('short_description', 'teams')

#Exemplo
    """protocol = random_protocol_generate()
    status = False
    short_description = forms.CharField(label='Título', max_length=50)    
    description = forms.CharField(label='Descrição', widget=forms.Textarea)"""

    
