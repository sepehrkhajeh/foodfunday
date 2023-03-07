from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import ListView

from accounts.forms import UserForm

from .models import FoodModel
# Create your views here.


def foodlist(request):
    a = FoodModel.objects.all()
    foods = FoodModel.objects.filter(available=True, category=1)
    otherfoods = FoodModel.objects.filter(category=2,available=True)
    salad = FoodModel.objects.filter(available=True,category=3)
    drink = FoodModel.objects.filter(available=True,category=4)

    
    return render(request, 'home/index.html', {'foods': foods,'otherfoods':otherfoods, 'salad': salad,'drink':drink,'all':a})
    
    
    
def logout(request):
    logout(request)
    return redirect('home:index')