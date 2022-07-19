from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Здесь будет главная страница нашей соц-сети')

def group_posts(request, slug):
    return HttpResponse(f'Здесь будет cтраница сообщества {slug}')