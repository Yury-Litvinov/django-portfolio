from django.urls import path
from . import views  # точка, т.к. наш файл находится в той же папке, что и views.py

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
