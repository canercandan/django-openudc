from django.db import models

class Peer(models.Model):
    ip = models.GenericIPAddressField()
    port = models.SmallIntegerField()
    port.min_value = 1
    port.max_value = 65535

    def __unicode__(self):
        return '%s:%s' % (self.ip, self.port)
