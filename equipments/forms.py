from django import forms
from django.contrib.auth.models import User, Group

from .models import Equipment, Connection

class EquipmentForm(forms.ModelForm):      
    class Meta:
        model = Equipment
        fields = ('name', 'description', 'status', 'icon')

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection        
        fields = ('description', 'direction', 'equipment_left', 'equipment_right')        