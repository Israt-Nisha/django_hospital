from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('show_profile/', views.show_profile, name='ditail_profile'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
]