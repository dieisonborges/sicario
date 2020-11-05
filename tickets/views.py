from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.core import validators
from django.contrib import messages
from django.urls import reverse

from .models import Ticket, Action

from .forms import TicketForm, ActionForm

from .utils import random_protocol_generate

from core.decorators import require_group

# Create your views here.
@login_required
def index_tickets(request):    
    latest_ticket_list = Ticket.objects.order_by('-created_at')
    template = loader.get_template('tickets/index.html')
    context = {
        'latest_ticket_list': latest_ticket_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def create_ticket(request):
    template_name = 'tickets/create_update.html'
    context = {}
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.protocol = random_protocol_generate()
            f.status = True #Open
            f.save()
            messages.success(request, 'Adicionado com sucesso!')
    form = TicketForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def read_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'tickets/read.html', {'ticket': ticket})

@login_required
def update_ticket(request, ticket_id):
    template_name = 'tickets/create_update.html'
    context = {}
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modificado com sucesso!')        
            return HttpResponseRedirect(reverse('tickets:read_ticket', kwargs={'ticket_id': ticket_id}))
    form = TicketForm(instance=ticket)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    messages.success(request, 'Removido com sucesso!')        
    return HttpResponseRedirect(reverse('tickets:index_tickets'))

@login_required
def close_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = False #Close Ticket
    ticket.save()
    messages.success(request, 'Encerrado com sucesso!')        
    return HttpResponseRedirect(reverse('tickets:read_ticket', kwargs={'ticket_id': ticket_id}))

@login_required
def open_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = True #Open Ticket
    ticket.save()
    messages.success(request, 'Reaberto com sucesso!')        
    return HttpResponseRedirect(reverse('tickets:read_ticket', kwargs={'ticket_id': ticket_id}))

@login_required
def create_action(request, ticket_id):
    template_name = 'actions/create_update.html'
    context = {}
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ticket_id = ticket_id
            f.user = request.user
            f.save()
            messages.success(request, 'Adicionado com sucesso!')        
            return HttpResponseRedirect(reverse('tickets:read_ticket', kwargs={'ticket_id': ticket_id}))
        else:
            messages.warning(request, 'Houve um problema tente novamente')
    form = ActionForm()
    context['form'] = form
    context['ticket_id'] = ticket_id
    print(form.__dict__)
    return render(request, template_name, context)





"""
def list_categories(request):
    template_name = 'tasks/list_categories'
    categories = category.objects.filter(user=request.user)
    context = {
        'categories: categories
    }
    return render(request, template_name, context)

def create_ticket(request):
    template_name = 'tickets/create.html'
    context = {}
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.status = True
            f.protocol = "JKSHKS"
            f.save()
            messages.success(request, 'Armazenado com sucesso')        
    form = TicketForm()
    context['form'] = form
    return render(request, template_name, context)
"""