from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from patient.forms import PatientForm
from patient.models import UserPatientDetails
from .models import Category

# Create your views here.
def show_category(request, category_slug=None):
    if category_slug : 
        category = get_object_or_404(Category, slug = category_slug)
        patients = UserPatientDetails.objects.filter(category=category)
    else:
        patients = UserPatientDetails.objects.all()
    categories = Category.objects.all()
    context = {'patients' : patients, 'categories' : categories, }
    
    return render(request, 'category/all_category.html', context)

def search(request):
    patients = UserPatientDetails.objects.none()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            patients= UserPatientDetails.objects.order_by('patient_id').filter(Q(description__icontains=keyword) | Q (first_name__icontains=keyword))
    context = {'patients' : patients, }
    return render(request, 'category/all_category.html', context)