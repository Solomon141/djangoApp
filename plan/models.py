from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plan(models.Model):
    class Meta:
        unique_together = (( 'pdate' ,'created_by' ),)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pdate = models.DateField(auto_now=False, auto_now_add=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    isApproved = models.BooleanField(null=True,default=False)
    sentToSuper = models.BooleanField(null=True,default=False)
    approvedBy = models.ForeignKey(User, related_name="approved_by", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return  f"{self.pdate}"