from django.db import models

# Create your models here.
class JobPosition(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class EntityType(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class DoctoralSpecialization(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class SalesType(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    

class CustomerClass(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name