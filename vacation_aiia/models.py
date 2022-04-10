import datetime

from django.db import models
from django.utils import timezone


class Vacation(models.Model):
    title = models.CharField("title", max_length=255, blank = True, null = True)
    description = models.CharField("description", max_length=255, blank = True, null = True)
    from_date = models.DateTimeField('from_Date');
    to_date = models.DateTimeField('to_Date');
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.from_date >= timezone.now() - datetime.timedelta(days=1)
    
