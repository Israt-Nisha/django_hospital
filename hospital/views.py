from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from patient.models import UserPatientDetails

def home(request):
    patients = UserPatientDetails.objects.all()
    user = request.user
    return render(request, 'index.html', {'patients' : patients})

