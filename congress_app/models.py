from django.db import models
from django.db.models.fields import DateTimeField
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
  def validate_registration(self, form):
    errors = {}
    if len(form['first_name']) < 2:
      errors['first_name'] = 'First name must be 2 characters'
    if len(form['last_name']) < 2:
      errors['last_name'] = 'Last name must be 2 characters'

    if not EMAIL_REGEX.match(form['email']):
      errors['email'] = 'Invalid Email Address'

    email_check = self.filter(email=form['email'])
    if email_check:
      errors['email'] = "Email already in use"

    if len(form['password']) < 8:
      errors['password'] = 'Password must be at least 8 characters'

    if form['password'] != form['confirm']:
      errors['password'] = 'Passwords do not match'
    return errors
  
  def authenticate(self, email, password):
    users = self.filter(email=email)
    if not users:
      return False
    
    user = users[0]
    return bcrypt.checkpw(password.encode(), user.password.encode())

class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  created_at = DateTimeField(auto_now_add=True, null=True)
  updated_at = DateTimeField(auto_now=True, null=True)

  objects = UserManager()

  def __str__(self):
    return f"{self.first_name} {self.last_name} {self.email}"
