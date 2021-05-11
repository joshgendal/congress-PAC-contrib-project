from django.shortcuts import render, redirect
from .models import User
import bcrypt

# Create your views here.
def index(request):
  return render(request, 'index.html')

def register(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
    return redirect('/register')  
  return render(request, 'register.html')