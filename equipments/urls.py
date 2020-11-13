from django.urls import path

from . import views

app_name = 'equipments'
urlpatterns = [
    #Equipments
    path('', views.index_equipments, name='index_equipments'),
    path('buscar/', views.search_equipment, name='search_equipment'),
    path('status/<str:status>/', views.filter_equipment_status, name='filter_equipment_status'),
    path('criar/equipment/', views.create_equipment, name='create_equipment'),
    path('<int:equipment_id>/', views.read_equipment, name='read_equipment'),    
    path('editar/<int:equipment_id>/', views.update_equipment, name='update_equipment'),
    path('delete/<int:equipment_id>/', views.delete_equipment, name='delete_equipment'),
    #Connection
    path('criar/<int:equipment_id>/conexao/', views.create_connection, name='create_connection'),
    path('delete/<int:equipment_id>/conexao/<int:connection_id>/', views.delete_connection, name='delete_connection'),
    path('editar/<int:equipment_id>/conexao/<int:connection_id>/', views.update_connection, name='update_connection'),
]