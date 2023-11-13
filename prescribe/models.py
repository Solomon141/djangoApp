from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prescribe(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    pres_code = models.CharField(max_length=10, null=True)
    hosp_name = models.CharField(max_length=255, null=True)
    patient_name = models.CharField(max_length=255, null=True)
    patient_phone = models.CharField(max_length=255, null=True)
    hosp_name = models.CharField(max_length=255, null=True)
    pdate = models.DateField(auto_now=False, auto_now_add=False)
    
    prescriber_name = models.CharField(max_length=255, null=True)
    prescriber_qualification = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return  f"{self.patient_name}"
    
    
class Drug(models.Model):
    pid = models.ForeignKey(Prescribe, on_delete=models.CASCADE)
    is_brand = models.BooleanField(default=False)
    brand_name = models.CharField(max_length=255, null=True)
    generic_name = models.CharField(max_length=255, null=True)
    sig = models.TextField()
    status =  models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return  f"{self.sig}"
    