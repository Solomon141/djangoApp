from django.db import models
from django.utils.timezone import now
from hospital.models import Hospital
# Create your models here.
class Doctor(models.Model):
    FullName = models.CharField(max_length=255, null=True)
    specialization = models.CharField(max_length=25, null=True)
    phoneNumber = models.CharField(max_length=255, null=True)
    dob = models.DateField(auto_now_add=True, null=True)
    hobby = models.CharField(max_length=25, null=True)
    region = models.CharField(max_length=25, null=True)
    orientation = models.CharField(max_length=25, null=True)
    customerClass = models.CharField(max_length=25, null=True)
    isClinicOwner = models.BooleanField(null=True, blank=True, default=False)
    hosp = models.ManyToManyField(Hospital, related_name="doctors")

    DisplayFields = ['FullName', 'phoneNumber']
    SearchFields = ['FullName', 'phoneNumber']

    def __str__(self):
        return f"{self.FullName}"