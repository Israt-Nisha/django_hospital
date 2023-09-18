from django.shortcuts import render,get_object_or_404, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from patient.models import UserPatientDetails



def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/register.html', {'form':form})

def show_profile(request):
    user = request.user
    patients= UserPatientDetails.objects.filter(user=user)
    return render(request, 'accounts/dashboard.html', {'data' : patients})


    
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/signin.html')

def user_logout(request):
    logout(request)
    return redirect('login')