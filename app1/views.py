from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Register,Login

# Create your views here.
def display(request):
    return render(request,'register.html')

def display1(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        phone=request.POST['Phone Number']
        username=request.POST['Username']
        password=request.POST['Password']
        data=Register.objects.create(name=name,email=email,phone=phone,username=username)
        data.save()
        data1=Login.objects.create(username=username,password=password)
        data1.save()
        return render(request,"login.html")

def login(request):
    if request.method == "POST":
        username=request.POST['Username']
        password=request.POST['Password']
        try:
            data1=Login.objects.get(username=username)
            if data1.password ==password:
                request.session['id']=username
                return redirect(index)
            else:
                return HttpResponse("password error")
        except Exception:
            return HttpResponse("username error")
    else:
     return render(request,'login.html')


def product(request):
    return render(request,'products.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def password(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        new=request.POST['new']
        try:
          data1= Login.objects.get(username=username)
          if data1.password==password:
            data1.password=new
            data1.save()
            context = {
            'msg': "Password changed successfully"
             }
            return render(request, 'change_password.html',context)
          else:
             return HttpResponse("password error")
        except Exception:
            return HttpResponse("username error")
    else:
        return redirect(changepassword)

def changepassword(request):
    return render(request,'change_password.html')

def product1(request):
    return render(request,'product1.html')

def product2(request):
    return render(request,'product2.html')

def product3(request):
    return render(request,'product3.html')

def product4(request):
    return render(request,'product4.html')

def product5(request):
    return render(request,'product5.html')

def product6(request):
    return render(request,'product6.html')

def product7(request):
    return render(request,'product7.html')

def product8(request):
    return render(request,'product8.html')

def product9(request):
    return render(request,'product9.html')

def product10(request):
    return render(request,'product10.html')

def product11(request):
    return render(request,'product11.html')

def library(request):
    return render(request,'librarian_interface.html')

def profile(request):
    if request.method == "POST":
        username = request.POST['username']
        newname=request.POST['newname']
        newemail=request.POST['newemail']
        newphone=request.POST['newphone']
        # newuser=request.POST['newuser']
        try:
          data= Register.objects.get(username=username)
          if data.username==username:
            data.name=newname
            data.email=newemail
            data.phone=newphone
            # data.username=newuser
            data.save()
            context = {
            'msg': "Information updated succesfully!"
             }
            return render(request, 'profile.html',context)
          else:
              context = {
                  'msg': "Username Error"
              }
              return render(request, 'profile.html', context)
        except Exception:
            context = {
                'msg': "Username Error"
            }
            return render(request, 'profile.html', context)
    else:
        return render(request,'profile.html')


def history(request):
    return render(request,'history.html')
