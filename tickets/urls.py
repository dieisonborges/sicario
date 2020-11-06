from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    #Tickets
    path('', views.index_tickets, name='index_tickets'),
    path('criar/ticket/', views.create_ticket, name='create_ticket'),
    path('<int:ticket_id>/', views.read_ticket, name='read_ticket'),    
    path('editar/<int:ticket_id>/', views.update_ticket, name='update_ticket'),
    path('delete/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('close/<int:ticket_id>/', views.close_ticket, name='close_ticket'),
    path('open/<int:ticket_id>/', views.open_ticket, name='open_ticket'),
    #Actions
    path('criar/ticket/<int:ticket_id>/acao/', views.create_action, name='create_action'),
    path('delete/ticket/<int:ticket_id>/acao/<int:action_id>', views.delete_action, name='delete_action'),
    path('editar/ticket/<int:ticket_id>/acao/<int:action_id>', views.update_action, name='update_action'),
]