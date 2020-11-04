from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib.auth.decorators import login_required

from tickets.models import Ticket


# Create your views here.

@login_required
def index(request):
    template_name = 'index.html'
    tickets_count_open = Ticket.objects.filter(status=True).count()
    tickets_count_close = Ticket.objects.filter(status=False).count()
    context = {
        'tickets_count_open': tickets_count_open,
        'tickets_count_close': tickets_count_close,
    }
    return render(request, template_name, context)