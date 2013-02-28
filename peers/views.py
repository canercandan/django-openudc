from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from models import Peer

def list(request):
    return render(request, 'peers/list.html', {'form': Peer(),})

def register(request):
    return render(request, 'peers/register.html')
