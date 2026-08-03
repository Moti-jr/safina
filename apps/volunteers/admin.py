from django.contrib import admin
from .models import VolunteerApplication


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'email', 'skills', 'status', 'created_at']
    list_editable = ['status']
    list_filter   = ['status', 'skills']
    search_fields = ['first_name', 'last_name', 'email']
    readonly_fields = [
        'first_name', 'last_name', 'email', 'phone',
        'skills', 'availability', 'motivation', 'created_at'
    ]
    fieldsets = (
        ('Applicant', {
            'fields': (
                'first_name', 'last_name',
                'email', 'phone'
            )
        }),
        ('Application', {
            'fields': ('skills', 'availability', 'motivation')
        }),
        ('Status', {
            'fields': ('status', 'created_at')
        }),
    )