from django import forms
from .models import ContactMessageModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessageModel
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ismingiz'
            }),
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Firmangizni Nomi'
            }),
            'lavozim': forms.TextInput(attrs={
                'placeholder': 'Lavozimingiz',
                'value': 'Menedjer',
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Telefon Raqamingiz',
                'value': '+998 '
            }),

            'message': forms.TextInput(attrs={
                'placeholder': 'Sovolingiz'
            }),
        }