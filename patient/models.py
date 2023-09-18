from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.

class UserPatientDetails(models.Model):
    GENDER_TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    patient_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.first_name