from django.contrib import admin
from .models import BloodDonor


@admin.register(BloodDonor)
class BloodDonorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'blood_group',
        'phone',
        'city',
        'available',
        'registered_date',
        'updated_date',
    )

    list_filter = (
        'blood_group',
        'available',
        'city',
        'registered_date',
    )

    search_fields = ('name', 'city', 'phone')

    date_hierarchy = 'registered_date'

    ordering = ('-registered_date',)
