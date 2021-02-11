from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import sign_up_form ,Log_in_form, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import blog_post
from django.contrib.auth.models import Group
from django.core.cache import cache
# Create your views here.

def Home(request):
    posts = blog_post.objects.all()
    return render(request, 'my_blog/home.html',{'posts':posts})

def About(request):
    return render(request, 'my_blog/about.html')

def Contact(request):
    return render(request, 'my_blog/contact.html')

def Dashboard(request):
    if request.user.is_authenticated:
        posts = blog_post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('IP', 0)
        ct = cache.get('count', version=user.pk)
        return render(request, 'my_blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'gps':gps, 'ip':ip, 'ct':ct})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_singup(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = sign_up_form(request.POST)
            if form.is_valid():
                user = form.save()
                group =Group.objects.get(name='Author')
                user.groups.add(group)
                messages.success(request,'Heyyy... Now You are Autor.')
                form = sign_up_form()
        else:
            form = sign_up_form()
        return render(request, 'my_blog/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Log_in_form(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Log In Successfully...')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = Log_in_form()
        return render(request, 'my_blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title =form.cleaned_data['title']
                desc =form.cleaned_data['desc']
                all_data = blog_post(title=title, desc=desc)
                all_data.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'my_blog/add_post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = blog_post.objects.get(pk = id)
            print('----2-----', pi)
            form =PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
            else:
                pi = blog_post.objects.get(pk=id)
                print('---1------',pi)
                form = PostForm(instance=pi)
        return render(request,'my_blog/update_post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = blog_post.objects.get(pk = id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
