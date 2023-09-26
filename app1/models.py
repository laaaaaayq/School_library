from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=50)
    # type=models.IntegerField()

    def __str__(self):
        return self.name

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Book(models.Model):
     bookname=models.CharField(max_length=100)
     author=models.CharField(max_length=100)
     description=models.CharField(max_length=1500)
     genre=models.CharField(max_length=100)
     image=models.ImageField()

     def __str__(self):
         return self.bookname