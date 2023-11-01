from django.db import models
from Lookups.models import Brand

# Create your models here.
class Badreg(models.Model):
    Brand_ID = models.ForeignKey(Brand, related_name="vendor", on_delete=models.PROTECT)
    pcode = models.CharField(max_length=15, null=True)
    pname = models.CharField(max_length=255, null=True)
    Compositions = models.TextField()
    UnitMeasure = models.CharField(max_length=255, null=True)
    paking = models.CharField(max_length=255, null=True)
    pksize = models.CharField(max_length=255, null=True)
    unitPrice = models.FloatField()
    MH_Count = models.IntegerField()
    badreg_Count = models.IntegerField()
    mh_stockout = models.BooleanField(null=True, blank=True, default=False)
    badreg_stockout = models.BooleanField(null=True, blank=True, default=False)
    expDate = models.CharField(max_length=255, null=True)
    criticalVal = models.CharField(max_length=255, null=True)
    img_hd = models.CharField(max_length=255, null=True)
    img_md = models.CharField(max_length=255, null=True)
    img_sm = models.CharField(max_length=255, null=True)
    img_blob = models.CharField(max_length=255, null=True)
    discount = models.FloatField(null=True)
    drugstore = models.BooleanField(null=True, blank=True, default=False)
    pharm = models.BooleanField(null=True, blank=True, default=False)
    pcat = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f"{self.pname}"
    
class Competitor(models.Model):
    badreg = models.ForeignKey(to=Badreg, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True)
    def __str__(self):
        return f"{self.name}"
    