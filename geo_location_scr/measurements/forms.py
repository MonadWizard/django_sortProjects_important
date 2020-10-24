from django import forms
from .models import Measurements

class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ('destination',)