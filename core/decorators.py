from django.http import HttpResponseRedirect, HttpResponse
from functools import wraps
from django.shortcuts import reverse
from django.contrib import messages
from django.contrib.auth.models import User, Group

def require_group(group=None):    
    pass