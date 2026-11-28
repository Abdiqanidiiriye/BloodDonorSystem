
import re

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

        labels = {
            'name': 'Full Name',
            'blood_group': 'Blood Group',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'city': 'City',
            'available': 'Available for Donation',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter donor full name'
            }),
            'blood_group': forms.Select(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. +252 61 234 5678'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email (optional)'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city'
            }),
            'available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if len(name) < 3:
            raise forms.ValidationError(
                'Name must be at least 3 characters long.'
            )

        if not re.match(r"^[A-Za-z .'-]+$", name):
            raise forms.ValidationError(
                'Name may only contain letters, spaces, dots, hyphens and apostrophes.'
            )

        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()
        digits = re.sub(r'\D', '', phone)

        if not re.match(r'^\+?[\d\s()-]+$', phone):
            raise forms.ValidationError(
                'Phone number may only contain digits, spaces, +, -, and brackets.'
            )

        if len(digits) < 7 or len(digits) > 15:
            raise forms.ValidationError(
                'Phone number must have between 7 and 15 digits.'
            )

        return phone

    def clean_city(self):
        city = self.cleaned_data['city'].strip()

        if not city:
            raise forms.ValidationError(
                'City cannot be empty.'
            )

        return city
