from statistics import mode
from tabnanny import verbose
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

def url_producto(self,filename):
    ruta = "static/img/productos/%s/%s"%(self.nombre, str(filename))
    return ruta

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=4)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=url_producto, blank=True)
    fk_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, default="")

    def imagen_producto(self):
        return mark_safe('<a href="/%s" target="_blank" > <img src="/%s" hight="50px" width="50px" ></a>'%(self.imagen,self.imagen))
    
    imagen_producto.allow_tags = True

    def __str__(self):
        return self.nombre


def url_perfil(self, filename):
    ruta = "static/img/perfiles/%s/%s"%(self.usuario, str(filename))
    return ruta

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    direccion = models.TextField()
    cedula = models.CharField(max_length=10)
    foto = models.ImageField(upload_to=url_perfil)

    def foto_perfil(self):
        return mark_safe('<a href="/%s" target="_blank" > <img src="/%s" hight="50px" width="50px" ></a>'%(self.foto, self.foto))
    
    foto_perfil.allow_tags = True

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return self.usuario.username

