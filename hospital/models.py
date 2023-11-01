from django.db import models
from area.models import Area
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phones = models.CharField(max_length=255, null=True, blank=True)
    latt = models.FloatField()
    longt = models.FloatField()
    tin = models.CharField(max_length=15)
    areaid = models.ForeignKey(Area, related_name="hospitals_in_area", on_delete=models.PROTECT)
    isApproved = models.BooleanField(null=True, blank=True, default=False)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    approved_at = models.DateTimeField(auto_now_add=True, null=True)

    DisplayFields = ['name', 'phones']
    SearchFields = ['name', 'phones']

    def __str__(self):
        return self.name
    
