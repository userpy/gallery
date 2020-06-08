from django.db import models

# Create your models here.




class Galary(models.Model):
    header = models.CharField(max_length=30, verbose_name='заголовок')
    image = models.FileField(upload_to='imageApp/', verbose_name='Картинка')
    def __str__(self):
        return self.header

