from django.contrib import admin
from .models import Arm

@admin.register(Arm)
class ArmAdmin(admin.ModelAdmin):
    list_display = ('regimental_number', 'name', 'rank', 'unit', 'arm_type', 'arm_status', 'location')
    search_fields = ('name', 'location', 'rank')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'regimental_number', 'rank', 'gender', 'unit', 'location')
        }),
        ('Arms Information', {
            'fields': ('arm_type', 'arm_action', 'arm_status', 'arm_source', 'ammunition_status', 'archive_reason')
        }),
        ('Identification', {
            'fields': ('id_types',)  
        }),
        ('Additional Information', {
            'fields': ('license_type', 'genuine_reason')
        })
    )
