from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    #If Logout
    path("criar/", views.create_user, name="create_user"),
    #
    path("editar/", views.update_user, name="update_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("modificar_senha/", views.password_reset_user, name="password_reset_user"),    
    path("perfil/criar/", views.create_profile_user, name="create_profile_user"),
    path("perfil/editar/", views.update_profile_user, name="update_profile_user"),
    path("perfil/", views.read_profile_user, name="read_profile_user"),
]