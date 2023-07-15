from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout ## Se o,´prta
from django.contrib import messages
# Create your views here.
def home(request):
    
    return render(request,'home.html',{})

def login_user():
    pass

def logout_user():
    pass