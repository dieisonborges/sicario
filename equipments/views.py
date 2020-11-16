from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.core import validators
from django.contrib import messages
from django.urls import reverse
from datetime import datetime, date
from django.db.models import Q


from .models import Equipment, Connection

from .forms import EquipmentForm, ConnectionForm

# Create your views here.
@login_required
def index_equipments(request):    
    template = loader.get_template('equipments/index.html')
    equipments = Equipment.objects.order_by('-created_at')
    equipments_count_operational = Equipment.objects.filter(status=1).count()
    equipments_count_partial_dead = Equipment.objects.filter(status=2).count()
    equipments_count_dead = Equipment.objects.filter(status=3).count()
    context = {
        'equipments_count_operational': equipments_count_operational,
        'equipments_count_partial_dead': equipments_count_partial_dead,
        'equipments_count_dead': equipments_count_dead,
        'equipments': equipments,
    }
    return HttpResponse(template.render(context, request))

@login_required
def search_equipment(request):
    template_name = 'equipments/index.html'
    equipments = Equipment.objects.order_by('-created_at')
    equipments_count_operational = Equipment.objects.filter(status=1).count()
    equipments_count_partial_dead = Equipment.objects.filter(status=2).count()
    equipments_count_dead = Equipment.objects.filter(status=3).count()
    search = request.GET.get('search')
    equipments = Equipment.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )
    context = {
        'equipments_count_operational': equipments_count_operational,
        'equipments_count_partial_dead': equipments_count_partial_dead,
        'equipments_count_dead': equipments_count_dead,
        'equipments': equipments,
    }
    return render(request, template_name, context)

@login_required
def filter_equipment_status(request, status):
    template_name = 'equipments/index.html'
    equipments = Equipment.objects.order_by('-created_at')
    equipments_count_operational = Equipment.objects.filter(status=1).count()
    equipments_count_partial_dead = Equipment.objects.filter(status=2).count()
    equipments_count_dead = Equipment.objects.filter(status=3).count()
    equipments = Equipment.objects.filter(status=status)
    context = {
        'equipments_count_operational': equipments_count_operational,
        'equipments_count_partial_dead': equipments_count_partial_dead,
        'equipments_count_dead': equipments_count_dead,
        'equipments': equipments,
    }
    return render(request, template_name, context)

@login_required
def create_equipment(request):
    template_name = 'equipments/create_update.html'
    context = {}
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.status = True #Open
            f.save()
            form.save_m2m()
            messages.success(request, 'Adicionado com sucesso!')
            return HttpResponseRedirect(reverse('equipments:index_equipments'))
        else:
            messages.error(request, 'Você não adiconou o Prazo')
    else:
        form = EquipmentForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def read_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)    
    context = {
        'equipment': equipment,
    }
    return render(request, 'equipments/read.html', context)

@login_required
def update_equipment(request, equipment_id):
    template_name = 'equipments/create_update.html'
    context = {}
    equipment = get_object_or_404(Equipment, id=equipment_id, user=request.user)
    if equipment.user == request.user:
        if request.method == 'POST':
            form = EquipmentForm(request.POST, request.FILES, instance=equipment)
            if form.is_valid():
                form.save()
                messages.success(request, 'Modificado com sucesso!')        
                return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))
        form = EquipmentForm(instance=equipment)
        context['form'] = form
        return render(request, template_name, context)
    else:
        messages.error(request, 'Você não tem permissão para esta ação')        
        return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))

@login_required
def delete_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    if equipment.user == request.user:
        equipment.delete()
        messages.success(request, 'Removido com sucesso!')        
        return HttpResponseRedirect(reverse('equipments:index_equipments'))
    else:
        messages.error(request, 'Você não tem permissão para esta ação')        
        return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))

@login_required
def create_connection(request, equipment_id):
    template_name = 'connections/create_update.html'
    context = {}
    if request.method == 'POST':
        form = ConnectionForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.equipment_id = equipment_id
            f.user = request.user
            f.save()
            messages.success(request, 'Adicionado com sucesso!')        
            return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))
        else:
            messages.warning(request, 'Houve um problema tente novamente')
    form = ConnectionForm()
    context['form'] = form
    context['equipment_id'] = equipment_id
    return render(request, template_name, context)

@login_required
def delete_connection(request, connection_id, equipment_id):
    connection = get_object_or_404(Connection, id=connection_id)
    if connection.user == request.user:
        connection.delete()
        messages.success(request, 'Removido com sucesso!')        
        return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))
    else:
        messages.error(request, 'Você não tem permissão para esta ação')        
        return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))

@login_required
def update_connection(request, equipment_id, connection_id):
    template_name = 'connections/create_update.html'
    context = {}
    connection = get_object_or_404(Connection, id=connection_id, user=request.user)
    if connection.user == request.user:
        if request.method == 'POST':
            form = ConnectionForm(request.POST, request.FILES, instance=connection)
            if form.is_valid():
                form.save()
                messages.success(request, 'Modificado com sucesso!')        
                return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))
        form = ConnectionForm(instance=connection)
        context['form'] = form
        return render(request, template_name, context)
    else:
        messages.error(request, 'Você não tem permissão para esta ação')        
        return HttpResponseRedirect(reverse('equipments:read_equipment', kwargs={'equipment_id': equipment_id}))