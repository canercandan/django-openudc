from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# from models import Add, Lookup
from models import *

from udid2 import Udid2
__keys__ = [x for x in Udid2.HashedVerboseParser()()]

def list(request):
    return render(request, 'pks/list.html', {'keys': __keys__,})

def add(request):
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/pks/ok')
    else:
        form = Add()

    return render(request, 'pks/add.html', {'form': form, 'keys': __keys__,})

def lookup(request):
    if request.method == 'GET':
        form = Lookup(request.GET)
        if form.is_valid():
            return render(request, 'pks/list.html', {'form': form, 'keys': __keys__, 'search': form.cleaned_data['search'],})
    else:
        form = Lookup()
    return render(request, 'pks/list.html', {'keys': __keys__,})
