from django.contrib import admin
from .models import BloodDonor


@admin.register(BloodDonor)
class BloodDonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'phone', 'city', 'available', 'registered_date')
    list_filter = ('blood_group', 'available', 'city')
    search_fields = ('name', 'city', 'phone')
