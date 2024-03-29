from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # blank - открыть страницу в новой вкладке

    def __str__(self):
        return self.title  # выведет в панели администрирование название проекта, а не его номер
