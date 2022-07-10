from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader
from AppFamiliares.models import Familia


# Create your views here.

def datos(self):

    datos=Familia(integrante="Mamá", nombre="María", fecha_nacimiento="1951-10-26")
    datos.save()

    datos_1=Familia(integrante="Papá", nombre="Miguel", fecha_nacimiento="1948-11-15")
    datos_1.save()

    datos_2=Familia(integrante="Hermano", nombre="Andrés", fecha_nacimiento="1978-02-25")
    datos_2.save()

    diccionario={'datos':datos, 'datos_1':datos_1, 'datos_2':datos_2}
    

    plantilla=loader.get_template('Template.html')

    documento=plantilla.render(diccionario)
    
    return HttpResponse(documento)
