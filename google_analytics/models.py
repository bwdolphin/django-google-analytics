from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

class Analytics(models.Model):
    site = models.ForeignKey(Site)
    analytics_code = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return u"%s" % (self.analytics_code)
    
    class Meta:
        verbose_name_plural = "Analytics"

class session_variable(models.Model):
    slot = models.IntegerField()
    visitor_id = models.IntegerField()
    session_starttime = models.IntegerField()
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

class visitor_variable(models.Model):
    slot = models.IntegerField()
    visitor_id = models.IntegerField()
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
