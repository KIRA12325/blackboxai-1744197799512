from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.home), name='dashboard'),
    path('medications/', login_required(views.medication_list), name='medication_list'),
    path('medications/add/', login_required(views.add_medication), name='add_medication'),
    path('appointments/', login_required(views.appointment_list), name='appointment_list'),
    path('appointments/add/', login_required(views.add_appointment), name='add_appointment'),
    path('contacts/', login_required(views.contact_list), name='contact_list'),
    path('contacts/add/', login_required(views.add_contact), name='add_contact'),
    path('signup/', views.signup, name='signup'),
]
