from django import forms

from .utils import random_protocol_generate

class TicketForm(forms.Form):      
    protocol = random_protocol_generate()
    status = False
    short_description = forms.CharField(label='Título', max_length=50)    
    description = forms.CharField(label='Descrição', widget=forms.Textarea)
