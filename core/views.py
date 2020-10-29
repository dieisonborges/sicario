from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def Index(request):
    return render(request, 'index.html')