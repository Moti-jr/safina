from django import forms
from .models import VolunteerApplication


class VolunteerForm(forms.ModelForm):
    class Meta:
        model  = VolunteerApplication
        fields = [
            'first_name', 'last_name', 'email',
            'phone', 'skills', 'availability', 'motivation'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'First name',
            }),
            'last_name': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'Last name',
            }),
            'email': forms.EmailInput(attrs={
                'class':       'form-control',
                'placeholder': 'your@email.com',
            }),
            'phone': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': '+254 700 000 000',
            }),
            'skills': forms.Select(attrs={
                'class': 'form-select',
            }),
            'availability': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'e.g. Weekends, Monday mornings...',
            }),
            'motivation': forms.Textarea(attrs={
                'class':       'form-control',
                'placeholder': 'Tell us why you want to volunteer...',
                'rows':        5,
            }),
        }