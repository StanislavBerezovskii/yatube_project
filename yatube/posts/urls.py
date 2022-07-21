# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group-list', views.group_posts),
    path('base-template', views.show_base_template),
]