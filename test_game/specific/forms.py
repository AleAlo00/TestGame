# characteristics/forms.py
from django import forms
from .models import MySpecific

class MySpecificForm(forms.ModelForm):
    class Meta:
        model = MySpecific
        fields = ['id_charact', 'name']  
