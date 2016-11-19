from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Volunteer(models.Model):
    emailAddr = models.EmailField (max_length=75)
    dateJoined = models.DateTimeField (auto_now_add=True)
    timezone = models.CharField (max_length=6)
    firstReminderTime = models.DateTimeField ()
    nextReminderTime = models.DateTimeField ()
    phoneNumber = models.CharField (max_length=16, blank=True, null=True)
    active = models.BooleanField (default=True)
    zipcode = models.CharField (max_length=10, blank=True, null=True)
    addr1 = models.CharField (max_length=200, blank=True, null=True)
    addr2 = models.CharField (max_length=200, blank=True, null=True)
    city = models.CharField (max_length=100, blank=True, null=True)
    state = models.CharField (max_length=2, blank=True, null=True)
    nonUS = models.BooleanField (default=False)
