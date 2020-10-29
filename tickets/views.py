from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core import validators
from django.contrib import messages

from .models import Ticket, Action
from .forms import TicketForm


# Create your views here.

def index(request):    
    latest_ticket_list = Ticket.objects.order_by('-created_at')[:5]
    template = loader.get_template('tickets/index.html')
    context = {
        'latest_ticket_list': latest_ticket_list,
    }
    return HttpResponse(template.render(context, request))

def read(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'tickets/read.html', {'ticket': ticket})

def create(request):
    template_name = 'tickets/create.html'
    context = {}
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            messages.success(request, 'Armazenado com sucesso')        
    form = TicketForm()
    context['form'] = form
    return render(request, template_name, context)