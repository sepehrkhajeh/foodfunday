from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import UserForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'ثبت نام با موفقیت انجام شد به رستوران ما خوش آمدید')
            return redirect('home:index')
        messages.error(request,  form.errors)
        messages.error(request, "ثبت نام موفقیت آمیز نبود لطفا در وارد کردن اطلاعات دقت نماید")
    form = UserForm()
    return render(request, 'accounts/register.html', {'form':form})


def Login(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    user = authenticate(request,phone=phone, password=password)    
    if user is not None:
        login(request,user)
        return redirect('home:index')
    return render(request, 'accounts/login.html',{})

def prof(request):
    return render(request, 'accounts/Adminlte.html',{})