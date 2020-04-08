from django.forms import ModelForm
from django import forms
from business.models import Products

class UpdateForm(ModelForm):
    class Meta:
        model=Products
        fields=['item','category','price','discount_price','image','description']
