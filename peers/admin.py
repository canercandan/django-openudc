from peers.models import Peer
from django.contrib import admin

class PeerAdmin(admin.ModelAdmin):
    fieldsets = []
    list_display = ('ip', 'port')

admin.site.register(Peer, PeerAdmin)
