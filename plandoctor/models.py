from django.db import models
from product.models import Badreg
from doctor.models import Doctor
from plan.models import Plan

# Create your models here.
class PlanDoctor(models.Model):
    planid = models.ForeignKey(Plan, related_name="plandoctor", on_delete=models.CASCADE)
    doctors = models.ForeignKey(Doctor, related_name="plandoctor", on_delete=models.CASCADE)
    products = models.ForeignKey(Badreg, related_name="products", on_delete=models.CASCADE)
    purpose = models.TextField()
    def __str__(self):
        return f"{self.purpose}"