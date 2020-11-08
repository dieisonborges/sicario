from django.contrib import admin
from .models import Ticket, Action

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ['short_description', 'description', 'user']
    search_fields =  ['short_description', 'description']

class ActionAdmin(admin.ModelAdmin):
    list_display = ['short_description', 'description', 'user']
    search_fields =  ['short_description', 'description']
    list_filter = ['user']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Action, ActionAdmin)
