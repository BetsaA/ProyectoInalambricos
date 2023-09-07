from django.db import models
import bluetooth as bt

# Create your models here.

class dispositivo(models.Model):
    nombre = models.CharField(max_length=50)
    MAC = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre



