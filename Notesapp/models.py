from django.db import models

# Create your models here.

class Userdetails(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.fullname
    
class Usernotes(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    email=models.EmailField(max_length=50)

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title