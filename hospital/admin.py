from django.contrib import admin
from .models import Hospital

# Register your models here.
# admin.site.register(Hospital)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = Hospital.DisplayFields
    search_fields = Hospital.SearchFields