from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Register,Book,Issue

# Create your views here.
def display(request):
    return render(request,'register.html')


def backtoregister(request):
    return redirect(display)

def display1(request):
    if request.method=="POST":
        try:
            name=request.POST['Name']
            email=request.POST['Email']
            phone=request.POST['Phone Number']
            username=request.POST['Username']
            password=request.POST['Password']
            data=Register.objects.create(name=name,email=email,phone=phone,username=username,password=password,type=1)
            data.save()
            return render(request, "login.html")
        except Exception:
            return render(request,'register.html',{'note':"username already exists!"})
    else:
        return redirect(backtoregister)


def login(request):
    if request.method == "POST":
        username=request.POST['Username']
        password=request.POST['Password']
        try:
            data1=Register.objects.get(username=username)
            if data1.password ==password:
                request.session['id']=data1.id
                if data1.type==1:
                    return redirect(index)
                else:
                    return redirect(library)
            else:
                return render(request,'login.html',{'msg':"password error"})
        except Exception:
            return render(request,'login.html',{'msg1':"username error"})
    else:
     return render(request,'login.html')


def product(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
            data1 = Book.objects.all()
            context = {
                'user':data,
                'books':data1
            }
            return render(request,'products.html',context)
    else:
        return redirect(login)



def index(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
            data1 = Book.objects.all()
            context = {
                'user': data,
                'books': data1
            }
            return render(request, 'index.html', context)
    else:
        return redirect(login)

def about(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
            return render(request,'about.html',{'data':data})
    else:
        return redirect(login)

def contact(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
            return render(request,'contact.html',{'data':data})
    else:
        return redirect(login)

def password(request):
    if 'id' in request.session:
        user=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=user)
            return render(request,'change_password.html',{'data':data})
        if request.method == "POST":
            password=request.POST['password']
            new=request.POST['new']
            data = Register.objects.get(id=user)
            try:
                data= Register.objects.get(id=user)
                if data.password==password:
                    data.password=new
                    data.save()
                    context = {
                        'msg': "Password changed successfully",
                        'data':data
                     }
                    return render(request, 'change_password.html',context)
                else:
                    context = {
                        'msg': "Password Error",
                        'data': data
                    }
                    return render(request, 'change_password.html',context)
            except Exception:
                context = {
                    'msg': "Id Error",
                    'data': data
                }
                return render(request, 'change_password.html',context)
    else:
        return redirect(login)


def changepassword(request):
    if 'id' in request.session:
        username = request.session['id']
        if request.method == 'GET':
            data = Register.objects.get(id=username)
            return render(request, 'change_password.html', {'data': data})
    else:
        return redirect(login)

def product1(request,id):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
            data1=Book.objects.get(id=id)
            context = {
                'user': data,
                'books': data1
            }
            return render(request,'product1.html',context)
    else:
        return redirect(login)


def library(request):
    if 'id' in request.session:
        data=Book.objects.all()
        return render(request,'librarian_interface.html',{'data':data})
    else:
        return redirect(login)

def profile(request):
    if 'id' in request.session:
        user=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=user)
            return render(request,'profile.html',{'data':data})
        if request.method == "POST":
            newname=request.POST['newname']
            newemail=request.POST['newemail']
            newphone=request.POST['newphone']
            data = Register.objects.get(id=user)
            try:
                data= Register.objects.get(id=user)
                data.name=newname
                data.email=newemail
                data.phone=newphone
                data.save()
                context = {
                    'data':data,
                    'msg': "Information updated succesfully!"
                 }
                return render(request, 'profile.html',context)
            except Exception:
                context = {
                    'msg': "Username Error",
                    'data': data
                }
                return render(request, 'profile.html', context)
    else:
        return redirect(login)


def history(request):
    if 'id' in request.session:
        data=Issue.objects.all()
        return render(request,'history.html',{'data':data})
    else:
        return redirect(login)


def user_history(request):
    if 'id' in request.session:
        username=request.session['id']
        if request.method =='GET':
            data=Register.objects.get(id=username)
            data1 = Issue.objects.filter(username=username).all()
            return render(request,'user_history.html',{'data':data,'data1':data1})
    else:
        return redirect(login)

def addbook(request):
    if 'id' in request.session:
        if request.method == "POST":
            bookname=request.POST['book']
            author=request.POST['author']
            description=request.POST['description']
            genre=request.POST['genre']
            image=request.FILES['image']
            data=Book.objects.create(bookname=bookname,author=author,description=description,genre=genre,image=image)
            data.save()
            return render(request,'addbooksuccess.html')
    else:
        return redirect(login)

def success(request):
    if 'id' in request.session:
        return render(request,'addbooksuccess.html')
    else:
        return redirect(login)



def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)
    else:
        return redirect(login)

def deletebook(request,id):
    if 'id' in request.session:
        data=Book.objects.get(id=id)
        data.delete()
        return redirect(library)
    else:
        return redirect(login)

def editbook(request,id):
    if 'id' in request.session:
        data=Book.objects.get(id=id)
        if request.method=="POST":
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
    else:
        return redirect(login)


def search(request):
    if 'id' in request.session:
        books=None
        search_data=None
        if request.method=="GET":
            search=request.GET.get('search')
            if search:
                search_data=Book.objects.filter(bookname__icontains=search)
            else:
                books=Book.objects.all()
        return render(request,'librarian_interface.html',{'books': books,'data': search_data})
    else:
        return redirect(login)


def getbook(request):
        if 'id' in request.session:
            userid = request.session['id']
            user=Register.objects.get(id=userid)
            if request.method=='POST':
                bookid=request.POST["bookid"]
                currentbook=Book.objects.get(id=bookid)
                if Issue.objects.filter(bookname=currentbook).exists():
                    return redirect(nobook)
                else:
                    data=Issue.objects.create(username=user, bookname=currentbook)
                    data.save()
                    return render(request,'issuebooksuccess.html')
        else:
            return redirect(login)

def returnbook(request,id):
    if 'id' in request.session:
        data1 = Issue.objects.get(id=id)
        data1.delete()
        return redirect(user_history)
    else:
        return redirect(login)

def nobook(request):
    if 'id' in request.session:
        return render(request,'nobook.html')
    else:
        return redirect(login)


