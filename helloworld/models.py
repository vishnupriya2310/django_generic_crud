from django.db import models
import datetime
# Create your models here.
class  Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.FileField(upload_to='profilepic/')
    dob = models.DateField(auto_now=False)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    

