from django import forms
from .models import DonationInquiry


class DonationForm(forms.ModelForm):
    class Meta:
        model  = DonationInquiry
        fields = [
            'name', 'email', 'phone',
            'donation_type', 'amount', 'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'Your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class':       'form-control',
                'placeholder': 'your@email.com',
            }),
            'phone': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': '+254 700 000 000',
            }),
            'donation_type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'amount': forms.NumberInput(attrs={
                'class':       'form-control',
                'placeholder': 'Amount in KES (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class':       'form-control',
                'placeholder': 'Any additional information...',
                'rows':        4,
            }),
        }