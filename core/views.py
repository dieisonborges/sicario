from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib.auth.decorators import login_required

from tickets.models import Ticket
from equipments.models import Equipment


# Create your views here.

@login_required
def index(request):
    template_name = 'index.html'
    tickets_open = Ticket.objects.filter(status=True)
    tickets_count_close = Ticket.objects.filter(status=False).count()
    equipments_success = Equipment.objects.filter(status="success").order_by('name')
    equipments_warning = Equipment.objects.filter(status="warning").order_by('name')
    equipments_danger = Equipment.objects.filter(status="danger").order_by('name')
    context = {
        'tickets_open': tickets_open,
        'tickets_count_close': tickets_count_close,
        'equipments_success': equipments_success,
        'equipments_warning': equipments_warning,
        'equipments_danger': equipments_danger,
    }
    return render(request, template_name, context)