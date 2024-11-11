from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,null=True)
    def _str_(self):
        return f'{self.Register_Number}'
from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    def __str__(self):
        return self.name

from django.db import models
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def str(self):
        return f"File uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
# adminapp/models.py


