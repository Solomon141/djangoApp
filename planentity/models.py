from django.db import models
from product.models import Badreg
from entity.models import Entity
from plan.models import Plan

# Create your models here.
class PlanEntity(models.Model):
    planid = models.ForeignKey(Plan, related_name="planentity", on_delete=models.CASCADE)
    entities = models.ForeignKey(Entity, related_name="entities", on_delete=models.CASCADE)
    products = models.ForeignKey(Badreg, related_name="entityproducts", on_delete=models.CASCADE)
    purpose = models.TextField()
    def __str__(self):
        return f"{self.purpose}"