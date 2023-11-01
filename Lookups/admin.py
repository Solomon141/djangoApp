from django.contrib import admin
from .models import Brand, EntityType, JobPosition, DoctoralSpecialization, SalesType, CustomerClass
# Register your models here.

admin.site.register(Brand)
admin.site.register(EntityType)
admin.site.register(JobPosition)
admin.site.register(DoctoralSpecialization)
admin.site.register(SalesType)
admin.site.register(CustomerClass)