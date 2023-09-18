from django.urls import path

from . import views

urlpatterns = [
    path('patient_details/', views.patient_detail, name='patient_details'),
    path('edit_patient/<int:pk>', views.PatientUpdate.as_view(), name='edit_patient'),
    path('delete_patient/<int:pk>', views.PatientDelete.as_view(), name='delete_patient'),

    
]