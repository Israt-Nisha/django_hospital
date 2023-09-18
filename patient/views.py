from django.shortcuts import render,get_object_or_404, redirect
from .forms import PatientForm
from .models import UserPatientDetails
from category.models import Category
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




class PatientUpdate(UpdateView):
    model = UserPatientDetails
    template_name = 'patient/patient_details.html'
    form_class = PatientForm
    success_url = reverse_lazy('ditail_profile')

class PatientDelete(DeleteView):
    model = UserPatientDetails
    template_name = 'patient/delete_patient.html'
    success_url = reverse_lazy('ditail_profile')
    
    
def patient_detail(request):
    form = PatientForm(request.POST)  

    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            saved_instance = form.save()  
            form.instance.patient_id = saved_instance.id
            form.save()
            return redirect('ditail_profile')

    return render(request, 'patient/patient_details.html', {'form': form})


