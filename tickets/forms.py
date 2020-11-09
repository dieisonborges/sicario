from django import forms
from django.contrib.auth.models import User, Group

from .utils import random_protocol_generate

from .models import Ticket, Action

class TicketForm(forms.ModelForm):      
    docfile = forms.FileField(label='Anexo', required=False)
    deadline = forms.DateTimeField(label='Prazo', required=False)
    class Meta:
        model = Ticket
        fields = ('short_description', 'description', 'docfile', 'teams', 'deadline')
        #exclude = ()

class ActionForm(forms.ModelForm): 
    docfile = forms.FileField(label='Anexo', required=False)
    class Meta:
        model = Action        
        fields = ('short_description', 'description', 'docfile', 'time')        
        #exclude = ()



#Exemplo
    """protocol = random_protocol_generate()
    status = False
    short_description = forms.CharField(label='Título', max_length=50)    
    description = forms.CharField(label='Descrição', widget=forms.Textarea)"""

    
