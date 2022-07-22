# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group-list/', views.group_posts, name='group-list'),
    path('base-template', views.show_base_template, name='base-template'),
]