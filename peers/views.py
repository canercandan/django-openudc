from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from models import Peer

from udid2 import Udid2
__keys__ = [x for x in Udid2.HashedVerboseParser()()]

def list(request):
    return render(request, 'peers/list.html', {'form': Peer(), 'keys': __keys__,})

def register(request):
    return render(request, 'peers/register.html', {'keys': __keys__,})
