"""Blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyBlog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('about/', views.About, name='About_Us'),
    path('contact/', views.Contact, name='Contact_Us'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('signup/', views.user_singup, name='sigup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_post/', views.add_post, name='add_post'),
    path('update_post/<int:id>', views.update_post, name='update_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
]
