from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = '/d/Dev/yatube_project/yatube/templates/posts/index.html'
    return render(request, template)

def group_posts(request, slug):
    return HttpResponse(f'Здесь будет cтраница сообщества {slug}')