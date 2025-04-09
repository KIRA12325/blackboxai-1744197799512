from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Medication, Appointment, EmergencyContact
from .forms import MedicationForm, AppointmentForm, EmergencyContactForm, SignUpForm
from django.contrib.auth import login
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'dashboard/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def medication_list(request):
    medications = Medication.objects.filter(user=request.user)
    return render(request, 'dashboard/medication_list.html', {'medications': medications})

@login_required
def add_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.user = request.user
            medication.save()
            return redirect('medication_list')
    else:
        form = MedicationForm()
    return render(request, 'dashboard/medication_form.html', {'form': form})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'dashboard/appointment_list.html', {'appointments': appointments})

@login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'dashboard/appointment_form.html', {'form': form})

@login_required
def contact_list(request):
    contacts = EmergencyContact.objects.filter(user=request.user)
    return render(request, 'dashboard/contact_list.html', {'contacts': contacts})

@login_required
def add_contact(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact_list')
    else:
        form = EmergencyContactForm()
    return render(request, 'dashboard/contact_form.html', {'form': form})
