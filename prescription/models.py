from django.db import models
from django.contrib.auth.models import User
from product.models import Badreg
from doctor.models import Doctor
from hospital.models import Hospital

# Create your models here.
class Prescription(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    pdate = models.DateField(auto_now=False, auto_now_add=False)
    doctor = models.ForeignKey(Doctor, related_name="pres_doctor", on_delete=models.CASCADE)
    product = models.ForeignKey(Badreg, related_name="pres_product", on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, related_name="pres_hosp", on_delete=models.CASCADE, null=True)
    p_fullname = models.CharField(max_length=50, null=True)
    p_age = models.CharField(max_length=50, null=True)
    qty = models.IntegerField()

    def __str__(self):
        return  f"{self.pdate}"