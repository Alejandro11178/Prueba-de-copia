from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class usuarioManager(BaseUserManager):
    def create_user(self,email, username, nombre, apellidos, password = None):
        if not email:
            raise ValueError('Debe poseer un Correo Electrónico')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombre = nombre,
            apellidos = apellidos
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, nombre, apellidos, password):
        user = self.create_user(
            email,
            username=username,
            nombre = nombre,
            apellidos=apellidos
        )
        user.usuario_admin = True
        user.set_password(password)
        user.save()
        return user
        


class usuario(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario',unique=True, max_length=50)
    email = models.EmailField('Correo Electrónico',unique=True, max_length=254)
    nombre = models.CharField('Nombre', max_length=50,blank=True, null=True)
    apellidos = models.CharField('Apellidos',max_length=200, blank=True, null=True)
    roles = (('',''),
             ('Alumno','Alumno'),
             ('Profesor','Profesor'))
    rol = models.TextField('rol', choices= roles ,max_length=8, default='')
    niveles = (('Elige un nivel educativo', 'Elige un nivel educativo'),
               ('Básica','Básica'),
               ('Media','Media'),
               ('Universitaria','Universitaria'))
    nivel = models.TextField(choices=niveles, default='Elige un nivel educativo')
    telefono = models.CharField('Teléfono', max_length=15, blank=True, null=True)
    materia = models.CharField('Materia', max_length=50, blank=True, null=True)
    horario = models.CharField('Horario de Atención', max_length=50, blank=True, null=True)
    precio = models.IntegerField('Precio',blank=True, null=True)
    usuario_activo = models.BooleanField(default= True)
    usuario_admin = models.BooleanField(default=False)
    objects = usuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre','apellidos']

    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellidos
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_admin
    

