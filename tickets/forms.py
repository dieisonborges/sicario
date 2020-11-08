from django import forms

from .utils import random_protocol_generate

from .models import Ticket, Action

class TicketForm(forms.ModelForm):      
    docfile = forms.FileField(label='Anexo', required=False)
    class Meta:
        model = Ticket
        fields = ('short_description', 'description', 'docfile')
        #exclude = ()

class ActionForm(forms.ModelForm): 
    docfile = forms.FileField(label='Anexo', required=False)
    class Meta:
        model = Action        
        fields = ('short_description', 'description', 'docfile')        
        #exclude = ()



#Exemplo
    """protocol = random_protocol_generate()
    status = False
    short_description = forms.CharField(label='Título', max_length=50)    
    description = forms.CharField(label='Descrição', widget=forms.Textarea)"""

    
