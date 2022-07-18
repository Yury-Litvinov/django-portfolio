from django.contrib import admin
from .models import Blog
# регистрация Моделей, которые мы хотим видеть в Админке для этого пользователя
admin.site.register(Blog)
