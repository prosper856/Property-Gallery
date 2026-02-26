from django import forms
from .models import Property, User
from django.contrib.auth.hashers import make_password, check_password


class BookForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ["name","location","description","image", "price","image","available",]