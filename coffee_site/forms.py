from django import forms
from .models import Customer
from django.core import validators


class FormName(forms.ModelForm):

    customer_name = forms.CharField()
    email = forms.EmailField(required=True)
    verify_email = forms.EmailField(label='Enter your email again')
    phone_number = forms.IntegerField(widget=forms.NumberInput(), required=True)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('email didnot match')

    class Meta():
        model = Customer
        fields = "__all__"
        widgets = {
            'customer_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'email':forms.EmailInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'verify_email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'phone_number':forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }
