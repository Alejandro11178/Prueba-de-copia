from django.shortcuts import render 
from usuario.models import usuario
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

class Home(ListView):
    usuarios = usuario.objects.all()
    niveles = usuario.niveles
    template_name = 'proyecto/index.html'
    
    def get_queryset(self):
        usuarios = self.usuarios.filter(rol = 'Profesor')
        nombre = self.request.GET.get('nombre','')
        nivel = self.request.GET.get('nivel','')
        materia = self.request.GET.get('materia','')
        valor = self.request.GET.get('valor','')
        valor2 = self.request.GET.get('valor2','')
        if nombre != '':
            # usuarios = self.usuarios.filter(nombre__icontains=nombre)
            usuarios = self.usuarios.filter(Q(nombre__icontains=nombre) | Q(apellidos__icontains=nombre))
            usuarios = usuarios.order_by('precio')
            
        if nivel != '':
            usuarios = self.usuarios.filter(nivel=nivel)
            usuarios = usuarios.order_by('precio')
        if materia != '':
            usuarios = self.usuarios.filter(materia=materia)
            usuarios = usuarios.order_by('precio')
        if valor and valor2:
            usuarios = usuarios.filter(precio__range=(valor, valor2))
            usuarios = usuarios.order_by('precio')
        elif valor:
            usuarios = usuarios.filter(precio__gte=valor)
            usuarios = usuarios.order_by('precio')
        elif valor2:
            usuarios = usuarios.filter(precio__lte=valor2)
            usuarios = usuarios.order_by('precio')
        return usuarios


def registro(request):
    return render(request, 'proyecto/registro.html')