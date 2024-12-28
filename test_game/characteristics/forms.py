# characteristics/forms.py
from django import forms
from .models import MyCharacteristics

class MyCharacteristicsForm(forms.ModelForm):
    class Meta:
        model = MyCharacteristics
        fields = ['id_cell', 'name']  
