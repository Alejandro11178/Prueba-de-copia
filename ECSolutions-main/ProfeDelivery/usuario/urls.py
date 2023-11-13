from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegistrarAlumno, RegistrarProfesor

urlpatterns = [
    path('registrarProfesor/', RegistrarProfesor.as_view(), name='RegistroP'),
    path('registrarAlumno/', RegistrarAlumno.as_view(), name='RegistroA')
]