from django.urls import path
from django.contrib.auth import views as auth_views #import this

from . import views

app_name = 'accounts'
urlpatterns = [
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("criar/", views.create_user, name="criar"),
    path("modificar_senha/", views.password_reset_user, name="password_reset_user"),    
]