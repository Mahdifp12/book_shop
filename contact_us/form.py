from django import forms
from django.forms import TextInput, EmailInput, Textarea
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["full_name", "email", "title", "message"]
