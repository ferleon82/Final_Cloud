from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from .models import Producto

    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username','password']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

