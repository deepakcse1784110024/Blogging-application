from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session

# Create your views here.

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('home')
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        count= User.objects.filter(email=email,password=password).count()
        if count>0:
            request.session['is_logged']=True
            request.session['user_id']=User.objects.values('id').filter(email=email,password=password)[0]['id']
            return redirect('home')
        else:
            messages.error(request,'invalid email or password')
            return redirect('login')
    return render(request,'studentbook/login.html')

def signup(request):
    return render(request,'studentbook/signup.html')

def register_user(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        obj =User(username=username,email=email,password=password)
        obj.save()
        messages.success(request,'signup successful')
        return redirect('login')


def home(request):
    if request.session.has_key('is_logged'):
        fetch_data=Blog.objects.all()

        return render(request,'studentbook/home.html',{'data':fetch_data})
    return redirect('login')


def logout(request):
    del request.session['is_logged']
    return redirect('login')

def create_post(request):
    if request.POST:
        good_name=request.POST['goodname']
        description =request.POST['description']
        title=request.POST['title']
        image=request.POST['image']
        user_id=request.session['user_id']

        obj = Blog(good_name=good_name,
                    description=description,
                    title=title,
                    image=image)
        obj.user_id_id=user_id 
        obj.save()   
        messages.success(request,"post added successfully") 
        return redirect('home')               
        
    return render(request,'studentbook/create_post.html')

def readmore(request,id):
    if request.POST:
        message=request.POST['message']
        user_id=request.POST['user_id']
        post_id=id
        query=Coment(message=message)
        
        query.post_id_id= post_id
        query.user_id_id= user_id
        query.save()
    data=Blog.objects.get(id=id)
    comment= Coment.objects.all().filter(post_id=id)
    return render(request,'studentbook/readmore.html',{'data':data,'comments':comment})

def developer(request):
    return render(request,'studentbook/developer.html')