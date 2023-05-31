from django.shortcuts import render
from django.http      import HttpResponse
from django.views     import generic
from atencion_medica.models import Cita, Consultorio, Departamento, Doctor, Paciente
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#Hrencia primero:LoginRequiredMixin
#Departamento
class DepartamentoListar(LoginRequiredMixin,generic.ListView):
    template_name = 'departamento/listar.html'
    model = Departamento
    context_object_name = 'depto'
    login_url = 'login'

#login_url = '/login'

class DepartamentoAgregar(LoginRequiredMixin,generic.CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/frmDepartamento.html'
    success_url   = reverse_lazy('departamento_listar')
    login_url = 'login'

class DepartamentoEditar(LoginRequiredMixin,generic.UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/frmDepartamento.html'
    success_url   = reverse_lazy('departamento_listar')
    login_url = 'login'

class DepartamentoEliminar(LoginRequiredMixin,generic.DeleteView):
    model = Departamento
    template_name = 'departamento/eliminar.html'
    context_object_name = 'depto'
    success_url   = reverse_lazy('departamento_listar')
    login_url = 'login'

#Consultorios
class ConsultorioListar(LoginRequiredMixin,generic.ListView):
    template_name = 'consultorio/listar.html'
    model = Consultorio
    context_object_name = 'consul'
    login_url = 'login'

class ConsultorioAgregar(LoginRequiredMixin,generic.CreateView):
    model = Consultorio
    form_class = ConsultorioForm
    template_name = 'consultorio/frmConsultorio.html'
    success_url   = reverse_lazy('consultorio_listar')
    login_url = 'login'

class ConsultorioEditar(LoginRequiredMixin,generic.UpdateView):
    model = Consultorio
    form_class = ConsultorioForm
    template_name = 'consultorio/frmConsultorio.html'
    success_url   = reverse_lazy('consultorio_listar')
    login_url = 'login'

class ConsultorioEliminar(LoginRequiredMixin,generic.DeleteView):
    model = Consultorio
    template_name = 'consultorio/eliminar.html'
    context_object_name = 'consul'
    success_url   = reverse_lazy('consultorio_listar')
    login_url = 'login'

#Doctores
class DoctorListar(LoginRequiredMixin,generic.ListView):
    template_name = 'doctor/listar.html'
    model = Doctor
    context_object_name = 'doc'
    login_url = 'login'

class DoctorAgregar(LoginRequiredMixin,generic.CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor/frmDoctor.html'
    success_url   = reverse_lazy('doctor_listar')
    login_url = 'login'

class DoctorEditar(LoginRequiredMixin,generic.UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor/frmDoctor.html'
    success_url   = reverse_lazy('doctor_listar')
    login_url = 'login'

class DoctorEliminar(LoginRequiredMixin,generic.DeleteView):
    model = Doctor
    template_name = 'doctor/eliminar.html'
    context_object_name = 'doc'
    success_url   = reverse_lazy('doctor_listar')
    login_url = 'login'

#Pacientes
class PacienteListar(LoginRequiredMixin,generic.ListView):
    template_name = 'paciente/listar.html'
    model = Paciente
    context_object_name = 'sick'
    login_url = 'login'

class PacienteAgregar(LoginRequiredMixin,generic.CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/frmPaciente.html'
    success_url   = reverse_lazy('paciente_listar')
    login_url = 'login'

class PacienteEditar(LoginRequiredMixin,generic.UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/frmPaciente.html'
    success_url   = reverse_lazy('paciente_listar')
    login_url = 'login'

class PacienteEliminar(LoginRequiredMixin,generic.DeleteView):
    model = Paciente
    template_name = 'paciente/eliminar.html'
    context_object_name = 'sick'
    success_url   = reverse_lazy('paciente_listar')
    login_url = 'login'

#Citas
class CitaListar(LoginRequiredMixin,generic.ListView):
    template_name = 'cita/listar.html'
    model = Cita
    context_object_name = 'cita'
    login_url = 'login'

class CitaAgregar(LoginRequiredMixin,generic.CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'cita/frmCita.html'
    success_url   = reverse_lazy('cita_listar')
    login_url = 'login'

class CitaEditar(LoginRequiredMixin,generic.UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'cita/frmCita.html'
    success_url   = reverse_lazy('cita_listar')
    login_url = 'login'

class CitaEliminar(LoginRequiredMixin,generic.DeleteView):
    model = Cita
    template_name = 'cita/eliminar.html'
    context_object_name = 'cita'
    success_url   = reverse_lazy('cita_listar')
    login_url = 'login'

#Usuarios
class RegistroUsuario(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'

