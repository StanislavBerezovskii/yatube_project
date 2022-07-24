# posts/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    title = 'Новости'
    text = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request):
    template = 'posts/group_list.html'
    title = 'Группы Yatube'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title' : title,
        'text' : text,
    }
    return render(request, template, context)

def show_base_template(request):
    template = 'base.html'
    return render(request,template)