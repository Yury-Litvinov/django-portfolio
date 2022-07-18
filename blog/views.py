from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
     # выведем не более 5 сообщений и отсортируем вывод так, что сверху
     # были самые свежие блоги
    # blogs = Blog.objects  # если не нужно настройки
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # функция get_object_or_404 ищет в калассе Blog Ищет в поле pk (это primary key) значение blog_id. А если не находит - выдает ошибку 404
    return render(request, 'blog/detail.html',{'blog':blog})
