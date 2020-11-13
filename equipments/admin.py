from django.contrib import admin
from .models import Equipment, Connection

# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields =  ['name', 'description']

class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields =  ['description']

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Connection, ConnectionAdmin)
