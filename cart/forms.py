from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    address = forms.CharField(max_length=300,required=True)
    class Meta:
        model = Orders
        fields = ('address',)
    