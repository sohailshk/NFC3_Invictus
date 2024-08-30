from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'photo', 'description', 'phone_number', 'email']