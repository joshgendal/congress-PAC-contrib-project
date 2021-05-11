from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
  return render(request, 'index.html')

def register(request):
  if request.method == "POST":
    # validate user info
    errors = User.objects.validate_registration(request.POST)
    if errors:
      for e in errors.values():
        messages.error(request, e)
      return redirect('/register')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
    return redirect('/register')  
  return render(request, 'register.html')

def login(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['password']
    if not User.objects.authenticate(email, password):
      messages.error(request, 'Invalid email/password')
      return redirect('/login')
    user = User.objects.get(email=email)
    messages.success(request, 'You have succesfully logged in')
    return redirect('/')
  return render(request, 'login.html')