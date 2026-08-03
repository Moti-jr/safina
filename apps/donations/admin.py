from django.contrib import admin
from .models import DonationInquiry


@admin.register(DonationInquiry)
class DonationInquiryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'donation_type', 'amount', 'status', 'created_at']
    list_editable = ['status']
    list_filter   = ['status', 'donation_type']
    search_fields = ['name', 'email']
    readonly_fields = [
        'name', 'email', 'phone',
        'donation_type', 'amount', 'message', 'created_at'
    ]
    fieldsets = (
        ('Donor', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Donation', {
            'fields': ('donation_type', 'amount', 'message', 'created_at')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )