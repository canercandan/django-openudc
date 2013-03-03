from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# from models import *

from udid2 import Udid2
__keys__ = [x for x in Udid2.ClearVerboseParser()()]

def home(request):
    return render(request, 'home.html', {'keys': __keys__,})

def capabilities(request):
    return render(request, 'capabilities.html', {'keys': __keys__,})
