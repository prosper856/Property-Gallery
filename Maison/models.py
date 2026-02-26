from django.db import models
from django.contrib.auth.models import User
CHOICES =[
    ("estate", "Estate"),
    ("villa", "Villa"),
    ("bungalow", "Bungalow"),
    ("duplex", "Duplex"),
    ("beach house", "Beach House"),
    ("cabin", "Cabin"),
    ("loft house", "Loft House")
]

class Agent(models.Model):
    name = models.CharField(max_length = 100, unique= True)
    bio = models.TextField()
    contact = models.CharField(max_length= 20)

    def __str__(self):
        return self.name


class Property(models.Model):
    name=models.CharField(max_length = 200, choices= CHOICES)
    owner= models.ForeignKey(Agent, on_delete=models.CASCADE)
    location=models.CharField(max_length = 150)
    description =models.TextField()
    price=models.DecimalField(max_digits= 10, decimal_places=2)
    available=models.BooleanField(default=True)
    image=models.ImageField(upload_to='housing/', blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name
