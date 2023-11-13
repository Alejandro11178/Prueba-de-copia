from typing import Any
from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from .models import usuario

class FormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class ProfesorForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña...',
            'id' : 'password1',
            'required' : 'required',
        }
        
    ))
    password2 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese nuevamente su contraseña...',
            'id' : 'password2',
            'required' : 'required',
        }
        
    ))

    class Meta:
        model = usuario
        fields = ['username','email','nombre','apellidos','nivel','telefono','materia','horario','precio']
        widgets = {
            'username' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Nombre de Usuario'
               } 
            ),
            'email' : forms.EmailInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Correo Electrónico'
               } 
            ),
            'nombre' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Nombre'
               } 
            ),
            'apellidos' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Apellidos'
               } 
            ),
            'nivel' : forms.Select(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Elegir Nivel Educativo'
               } 
            ),
            'telefono' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Teléfono'
               } 
            ),
            'materia' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Materia'
               } 
            ),
            'horario' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Horario'
               } 
            ),
            'Precio' : forms.NumberInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Precio'
               } 
            )
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.rol = 'Profesor'
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AlumnoForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña...',
            'id' : 'password1',
            'required' : 'required',
        }
        
    ))
    password2 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese nuevamente su contraseña...',
            'id' : 'password2',
            'required' : 'required',
        }
        
    ))

    class Meta:
        model = usuario
        fields = ['username','email','nombre','apellidos','nivel','telefono']
        widgets = {
            'username' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Nombre de Usuario'
               } 
            ),
            'email' : forms.EmailInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Correo Electrónico'
               } 
            ),
            'nombre' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Nombre'
               } 
            ),
            'apellidos' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Apellidos'
               } 
            ),
            'nivel' : forms.Select(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Elegir Nivel Educativo'
               } 
            ),
            'telefono' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : 'Teléfono'
               } 
            )
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.rol = 'Alumno'
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user