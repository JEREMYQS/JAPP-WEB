from django.db import models


class Practica(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

