from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Record(models.Model):
    created_at =models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city =  models.CharField(max_length=50, default=True)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    