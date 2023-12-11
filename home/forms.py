# forms.py
from django import forms
from .models import member

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = member
        fields = ['name', 'card_no', 'user', 'phone', 'address', 'weight', 'height', 'blood_groups', 'biceps']
