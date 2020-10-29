from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ticket_id>/', views.read, name='read'),
    path('create/', views.create, name='create'),
]