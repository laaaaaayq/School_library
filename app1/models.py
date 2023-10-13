from django.db import models
from datetime import date
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    type = models.IntegerField(null=True)

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


class Issue(models.Model):
    username=models.ForeignKey(Register,on_delete=models.CASCADE)
    bookname=models.ForeignKey(Book,on_delete=models.CASCADE)
    issuedate=models.DateField(default=date.today,blank=False)

    def __str__(self):
        return self.username.username +" "+ "took" + " "+ self.bookname.bookname

