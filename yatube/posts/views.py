from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader

# Create your views here.
def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = loader.get_template('posts/index.html')
    # Формируем шаблон
    return HttpResponse(template.render({}, request)) 

def group_posts(request, slug):
    return HttpResponse(f'Здесь будет cтраница сообщества {slug}')