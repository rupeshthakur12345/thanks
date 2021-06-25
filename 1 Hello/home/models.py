from django.db import models
from django.db.models.base import Model

# Create your models here.



class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=15)
    phone=models.CharField(max_length=13)
    desc=models.TextField(max_length=500)
    date=models.DateField()
    
    

    # if come in database object 1 object 2 so there is come like name so add this __str__ function 
    def __str__(self):
        return self.name
    
