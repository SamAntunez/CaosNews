from django.db import models

# Create your models here.
class TipoNoticia(models.Model):
    nombre = models.CharField(primary_key=True,max_length=50)
    
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='noticias',null=True)
    tipo = models.ForeignKey(TipoNoticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre