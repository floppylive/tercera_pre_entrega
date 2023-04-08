from django.db import models

# Create your models here.


class Frase(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    frase =models.CharField(max_length=140)
    privado = models.BooleanField()
    
    def __str__(self):
        return f'Soy {self.nombre}, tengo {self.edad} y yo digo que {self.frase}'
    
class Moderador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    
    def __str__(self):
        return f'Soy {self.nombre} {self.apellido}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    inhabilitado=models.BooleanField()
    
    def __str__(self):
        return f'Soy {self.nombre} {self.apellido}'