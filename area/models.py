from django.db import models

# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Area(models.Model):
    zone = models.ForeignKey(to=Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"