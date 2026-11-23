from django import forms
from .models import BloodDonor


class DonorForm(forms.ModelForm):

    class Meta:
        model = BloodDonor

        fields = [
            'name',
            'blood_group',
            'phone',
            'email',
            'city',
            'available'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter donor name'
            }),

            'blood_group': forms.Select(attrs={
                'class': 'form-control'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city'
            }),
        }