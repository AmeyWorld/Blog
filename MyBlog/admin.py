from django.contrib import admin
from .models import blog_post
# Register your models here.

@admin.register(blog_post)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','title','desc')