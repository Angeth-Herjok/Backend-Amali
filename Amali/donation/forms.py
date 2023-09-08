from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('amount')
    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)