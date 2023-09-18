from django.urls import path
from . import views
urlpatterns = [
    path('category_patient/', views.show_category, name = 'all_category'),
    path('category_patient/category/<slug:category_slug>/', views.show_category, name = 'patient_by_category'),
    path('search/', views.search, name='search'),
]