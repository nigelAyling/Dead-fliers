from django import forms
from.import models

class AirmenForm(forms.ModelForm):
    class Meta:
        model = models.Airmen
        fields=['surname','first_names','rank','service_number','date',
        'age','unit','cemetery','aircraft','serial_no','base','circumstance']
