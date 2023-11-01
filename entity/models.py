from django.db import models
from django.contrib.auth.models import User
from area.models import Area
from Lookups.models import JobPosition, CustomerClass, EntityType

# Create your models here.
class Entity(models.Model):
    Custname = models.CharField(max_length=255, null=True)
    TinNum = models.CharField(max_length=255, null=True)
    PhoneNum = models.CharField(max_length=255, null=True)
    Addr = models.CharField(max_length=255, null=True)
    ZoneID = models.IntegerField(null=True)
    area = models.ForeignKey(Area, related_name="entity_in_area", on_delete=models.CASCADE, null=True, blank=True)
    compType = models.ForeignKey(EntityType, related_name="bentity", on_delete=models.CASCADE, null=True, blank=True)
    insertedBy = models.ForeignKey(User, related_name="bentity_insert", on_delete=models.CASCADE, null=True, blank=True)
    Inserted_Date = models.DateTimeField(auto_now_add=True, null=True)
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    customerClass = models.ForeignKey(CustomerClass, related_name="bentity", on_delete=models.CASCADE, null=True, blank=True)
    approvedBy = models.ForeignKey(User, related_name="bentity_approve", on_delete=models.CASCADE, null=True, blank=True)
    isApproved = models.BooleanField(null=True, blank=True, default=False)
    
    def __str__(self):
        return self.Custname

class ContactPerson(models.Model):
    created_by = models.ForeignKey(Entity, related_name="contactperson", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    Position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    Profession = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    def __str__(self):
        return self.name