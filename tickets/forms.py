from django import forms

from .utils import random_protocol_generate

from .models import Ticket, Action

class TicketForm(forms.ModelForm):      

    class Meta:
        model = Ticket
        fields = ('short_description', 'description')
        #exclude = ()

class ActionForm(forms.ModelForm):      

    class Meta:
        model = Action
        fields = ('short_description', 'description')
        #exclude = ()



#Exemplo
    """protocol = random_protocol_generate()
    status = False
    short_description = forms.CharField(label='Título', max_length=50)    
    description = forms.CharField(label='Descrição', widget=forms.Textarea)"""
