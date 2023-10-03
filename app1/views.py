from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Register,Login,Book

# Create your views here.
def display(request):
    return render(request,'register.html')


def backtoregister(request):
    return redirect(display)

def display1(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        phone=request.POST['Phone Number']
        username=request.POST['Username']
        password=request.POST['Password']
        data=Register.objects.create(name=name,email=email,phone=phone,username=username)
        data.save()
        data1=Login.objects.create(username=username,password=password,type=1)
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
                if data1.type==1:
                    return redirect(index)
                else:
                    return redirect(library)
            else:
                return HttpResponse("password error")
        except Exception:
            return HttpResponse("username error")
    else:
     return render(request,'login.html')


def product(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            data1 = Book.objects.all()
            context = {
                'user':data,
                'books':data1
            }
            return render(request,'products.html',context)



def index(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            data1 = Book.objects.all()
            context = {
                'user': data,
                'books': data1
            }
            return render(request, 'index.html', context)
    # data1 = Book.objects.all()
    # return render(request, 'index.html', {'data2': data1})

def about(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            return render(request,'about.html',{'data':data})
    # return render(request,'about.html')

def contact(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            return render(request,'contact.html',{'data':data})
    # return render(request,'contact.html')

def password(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            return render(request,'change_password.html',{'data':data})
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
    if 'id' in request.session:
        username = request.session['id']
        if request.method == 'GET':
            data = Register.objects.filter(username=username).all()
            return render(request, 'change_password.html', {'data': data})
    # return render(request,'change_password.html')

def product1(request,id):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            data1=Book.objects.get(id=id)
            context = {
                'user': data,
                'books': data1
            }
            return render(request,'product1.html',context)


def library(request):
    data=Book.objects.all()
    return render(request,'librarian_interface.html',{'data':data})

def profile(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            return render(request,'profile.html',{'data':data})
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
def user_history(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(username=username).all()
            return render(request,'user_history.html',{'data':data})
    # return render(request,'user_history.html')


def addbook(request):
    if request.method == "POST":
        bookname=request.POST['book']
        author=request.POST['author']
        description=request.POST['description']
        genre=request.POST['genre']
        image=request.FILES['image']
        data=Book.objects.create(bookname=bookname,author=author,description=description,genre=genre,image=image)
        data.save()
        return render(request,'addbooksuccess.html')

def success(request):
    return render(request,'addbooksuccess.html')

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)

def deletebook(request,id):
    data=Book.objects.get(id=id)
    data.delete()
    return redirect(library)


def editbook(request,id):
    data=Book.objects.get(id=id)
    if request.method=="POST":
        # book=request.POST['book']
        newbook=request.POST['newbook']
        author=request.POST['newauthor']
        description=request.POST['newdescription']
        genre=request.POST['newgenre']
        image=request.FILES['newimage']
        try:
            data=Book.objects.get(id=id)
            if data.id==id:
                data.bookname=newbook
                data.author=author
                data.description=description
                data.genre=genre
                data.image=image
                data.save()
                return redirect(library)
            else:
                return HttpResponse("Book not found")
        except Exception:
            return HttpResponse("Check the book name")
    else:
        return render(request,'editbook.html',{'data':data})



def search(request):
    data=Book.objects.all()
    books=None
    search_data=None
    if request.method=="GET":
        search=request.GET.get('search')
        if search:
            search_data=Book.objects.filter(bookname__icontains=search)
        else:
            books=Book.objects.all()
    return render(request,'librarian_interface.html',{'books': books,'data': search_data})



def usersearch(request):
    if 'id' in request.session:
        username = request.session['id']
        if request.method == 'GET':
            data = Register.objects.filter(username=username).all()
            return render(request, 'products.html', {'user': data})
    data=Book.objects.all()
    books=None
    search_data=None
    if request.method=="GET":
        search=request.GET.get('search')
        if search:
            search_data=Book.objects.filter(bookname__icontains=search)
        else:
            books=Book.objects.all()
    return render(request,'products.html',{'books': books,'data': search_data})