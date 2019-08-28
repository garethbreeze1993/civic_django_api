from django.db import models
from django.utils import timezone


class Vote(models.Model):
    subject = models.CharField(max_length=256)
    vote_date = models.DateTimeField(default=timezone.now)
    ayes = models.PositiveSmallIntegerField(null=True, blank=True)
    nays = models.PositiveSmallIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.subject} - {self.ayes}/{self.nays} on {self.vote_date.strftime('%c')}"
    
    
