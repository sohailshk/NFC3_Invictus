from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['image', 'description', 'goal_amount', 'phone_number', 'email']