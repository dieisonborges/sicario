from django.urls import path

from . import views

app_name = 'teams'
urlpatterns = [
    #Tickets
    path('', views.index_tickets, name='index_teams'),
]