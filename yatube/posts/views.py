# posts/views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'Проект Yatube'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title' : title,
        'text': text,
    }
    return render(request, template, context) 

def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)

def show_base_template(request):
    template = 'base.html'
    return render(request,template)