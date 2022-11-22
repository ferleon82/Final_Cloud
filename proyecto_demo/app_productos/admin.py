from pyexpat import model
from django.contrib import admin
from .models import *
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin

#class ProductoResourse(resources.ModelResource):
#    class Meta:
#       model = Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','cantidad','precio','descripcion','fk_categoria','imagen_producto')
    search_fields = ['nombre']
    #resource_class = ProductoResourse

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    search_fields = ['nombre']



admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)

