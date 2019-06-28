from django.db import models

# Create your models here.

class Oncall(models.Model):
    title = models.CharField(max_length=200, default='')
    allDay = models.BooleanField(default=False)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)