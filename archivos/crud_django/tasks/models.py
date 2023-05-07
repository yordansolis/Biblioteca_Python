from django.db import models

# Create your models here.
#creado db
class Task(models.Model):
    title = models.CharField(max_length=200)#que tect y maximo
    description = models.TextField(blank=True) #que pueda svenir vacio
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.title
