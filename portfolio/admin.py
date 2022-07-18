from django.contrib import admin
from .models import Project
# регистрация Моделей, которые мы хотим видеть в Админке для этого пользователя
admin.site.register(Project)
