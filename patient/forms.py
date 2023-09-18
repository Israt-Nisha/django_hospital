from django import forms
from .models import UserPatientDetails


class PatientForm(forms.ModelForm):
    class Meta:
        model = UserPatientDetails
        fields = ['first_name', 'patient_id', 'age', 'gender', 'phone', 'address', 'category', 'description']