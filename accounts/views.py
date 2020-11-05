from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import UserForm, UserProfileForm

from .models import UserProfile

# Create your views here.
def login_user(request):
	template_name = 'login.html'
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'Login efetuado com sucesso!')  
			return redirect(request.GET.get('next', '/'))
		else:
			messages.error(request, 'Usuário ou senha inválidos!')
	return render(request, template_name, {})

@login_required
def logout_user(request):
	logout(request)
	return redirect('accounts:login_user')

@login_required
def create_user(request):
	template_name = 'create_update.html'
	context = {}
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.set_password(f.password)
			f.save()
			messages.success(request, 'Adicionado com sucesso!')        
            #return HttpResponseRedirect(reverse('accounts:read_user', kwargs={'user_id': ticket_id}))
	form = UserForm()
	context['form'] = form
	return render(request, template_name, context)

@login_required
def password_reset_user(request):
	template_name = 'password_reset_user.html'
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, 'Adicionado com sucesso!')
		else:
			messages.error(request, 'Não foi possível alterar sua senha!')
	form = PasswordChangeForm(user=request.user)
	context['form'] = form
	return render(request, template_name, context)

@login_required
def create_profile_user(request):
	template_name = 'create_update_user_profile.html'
	context = {}
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.user = request.user
			f.save()
			messages.success(request, 'Adicionado com sucesso!')
		else:
			messages.error(request, 'Houve um erro!')      
	form = UserProfileForm()
	context['form'] = form
	return render(request, template_name, context)

@login_required
def read_profile_user(request):
	template_name = 'read_user_profile.html'	
	profile = UserProfile.objects.get(user=request.user)	
	context = {
		'profile': profile
	}
	return render(request, template_name, context)
	