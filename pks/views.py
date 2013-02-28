from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from models import Add, Lookup

def index(request):
    return render(request, 'pks/index.html', {'add': Add(), 'lookup': Lookup(),})

def add(request):
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/pks/ok')
    else:
        form = Add()

    return render(request, 'pks/add.html', {'form': form,})

def lookup(request):
    if request.method == 'GET':
        form = Lookup(request.GET)
        if form.is_valid():
            return HttpResponse('done: %s' % form.cleaned_data['search'])
    else:
        form = Lookup()

    return render(request, 'pks/lookup.html', {'form': form,})
