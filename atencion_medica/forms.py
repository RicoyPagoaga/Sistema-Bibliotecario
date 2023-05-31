
from django import forms
from .models import *

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model  = Departamento
        fields = ['Especialidad','concentracion']

    Especialidad = forms.CharField(label= 'Especialidad Departamento', widget=forms.TextInput(attrs={'class':'form-control'}))
    concentracion = forms.CharField(label= 'Concentración', widget=forms.TextInput(attrs={'class':'form-control'}))

class ConsultorioForm(forms.ModelForm):
    class Meta:
        model  = Consultorio
        fields = ['Jornada','Piso','NoDepto']

    Jornada = forms.CharField(label= 'Jornada', widget=forms.TextInput(attrs={'class':'form-control'}))
    Piso = forms.IntegerField(label= 'Piso', widget=forms.NumberInput(attrs={'class':'form-control'}))
    NoDepto = forms.ModelChoiceField(label= 'No. Departamento', widget=forms.Select(attrs={'class':'form-control'}), queryset= Departamento.objects.all())

class DoctorForm(forms.ModelForm):
    class Meta:
        model  = Doctor 
        fields = ['Nombres', 'Apellidos','FechaNac','Telefono','correo','FechaIngreso','NoConsultorio']
        labels = {'Nombres'  :'Nombre:',
                'Apellidos':'Apellido:',
                'FechaNac':'Fecha de Nacimiento:',
                'Telefono':'Teléfono:',
                'correo':'Correo Electrónico:',
                'FechaIngreso':'Fecha de Ingreso:',
                'NoConsultorio':'Consultorio:'
                 } 
        widget = {
                    'Nombres':forms.TextInput(attrs={'class':'form-control'}),
                    'Apellidos':forms.TextInput(attrs={'class':'form-control'}),
                    'FechaNac':forms.DateInput(attrs={'class':'form-control'}),
                    'Telefono':forms.TextInput(attrs={'class':'form-control'}),
                    'correo':forms.TextInput(attrs={'class':'form-control'}),
                    'FechaIngreso':forms.DateInput(attrs={'class':'form-control'}),
                    'NoConsultorio':forms.TextInput(attrs={'class':'form-control'})
                 }

class PacienteForm(forms.ModelForm):
    class Meta:
        model  = Paciente
        fields = ['DNI','Nombres','Apellidos','FechaNac','Telefono','correo','Direccion']

    DNI = forms.CharField(label= 'DNI', widget=forms.TextInput(attrs={'class':'form-control'}))
    Nombres = forms.CharField(label= 'Nombres', widget=forms.TextInput(attrs={'class':'form-control'}))
    Apellidos  = forms.CharField(label= 'Apellidos', widget=forms.TextInput(attrs={'class':'form-control'}))
    FechaNac  = forms.DateField(label= 'Fecha de Nacimiento:', widget=forms.DateInput(attrs={'class':'form-control'}))
    Telefono  = forms.CharField(label= 'Teléfono', widget=forms.TextInput(attrs={'class':'form-control'}))
    correo = forms.CharField(label= 'Correo Electrónico', widget=forms.TextInput(attrs={'class':'form-control'}))
    Direccion = forms.CharField(label= 'Direccion', widget=forms.TextInput(attrs={'class':'form-control'}))

class CitaForm(forms.ModelForm):
    class Meta:
        model  = Cita
        fields = ['FechaRegistro','FechaAtencion','DniPaciente','IdDoctor','Descripcion']
        labels = {'FechaRegistro'  :'Fecha De Registro:',
                'FechaAtencion':'Fecha De Atención:',
                'DniPaciente':'Paciente:',
                'IdDoctor':'Doctor:',
                'Descripcion':'Descripción:'
                 } 
        widget = {
                    'FechaRegistro':forms.DateInput(attrs={'class':'form-control'}),
                    'FechaAtencion':forms.DateTimeInput(attrs={'class':'form-control'}),
                    'DniPaciente':forms.Select(attrs={'class':'form-control'}),
                    'IdDoctor':forms.Select(attrs={'class':'form-control'}),
                    'Descripcion':forms.TextInput(attrs={'class':'form-control'})
                 }
