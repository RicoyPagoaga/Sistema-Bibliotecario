from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('healthcare/atencion_medica/departamentos/listar',           DepartamentoListar.as_view(),   name  = 'departamento_listar'),
    path('healthcare/atencion_medica/departamentos/agregar',          DepartamentoAgregar.as_view(),  name  = 'departamento_agregar'),
    path('healthcare/atencion_medica/departamentos/editar/<int:pk>',  DepartamentoEditar.as_view(),   name  = 'departamento_editar'),
    path('healthcare/atencion_medica/departamentos/eliminar/<int:pk>',DepartamentoEliminar.as_view(), name  = 'departamento_eliminar'),

    path('healthcare/atencion_medica/consultorios/listar' ,          ConsultorioListar.as_view(),    name  = 'consultorio_listar'),
    path('healthcare/atencion_medica/consultorios/agregar' ,         ConsultorioAgregar.as_view(),   name  = 'consultorio_agregar'),
    path('healthcare/atencion_medica/consultorios/editar/<int:pk>',  ConsultorioEditar.as_view(),    name  = 'consultorio_editar'),
    path('healthcare/atencion_medica/consultorios/eliminar/<int:pk>',ConsultorioEliminar.as_view(),  name  = 'consultorio_eliminar'),

    path('healthcare/atencion_medica/doctores/listar'            ,DoctorListar.as_view(),    name  = 'doctor_listar'),
    path('healthcare/atencion_medica/doctores/agregar'           ,DoctorAgregar.as_view(),   name  = 'doctor_agregar'),
    path('healthcare/atencion_medica/doctores/editar/<int:pk>'   ,DoctorEditar.as_view(),    name  = 'doctor_editar'),
    path('healthcare/atencion_medica/doctores/eliminar/<int:pk>' ,DoctorEliminar.as_view(),  name  = 'doctor_eliminar'),

    path('healthcare/atencion_medica/pacientes/listar'            ,PacienteListar.as_view(),   name  = 'paciente_listar'),
    path('healthcare/atencion_medica/pacientes/agregar'           ,PacienteAgregar.as_view(),  name  = 'paciente_agregar'),
    path('healthcare/atencion_medica/pacientes/editar/<str:pk>'   ,PacienteEditar.as_view(),   name  = 'paciente_editar'),
    path('healthcare/atencion_medica/pacientes/eliminar/<str:pk>' ,PacienteEliminar.as_view(), name  = 'paciente_eliminar'),

    path('healthcare/atencion_medica/citas/listar'           ,CitaListar.as_view(),   name  = 'cita_listar'),
    path('healthcare/atencion_medica/citas/agregar'          ,CitaAgregar.as_view(),  name  = 'cita_agregar'),
    path('healthcare/atencion_medica/citas/editar/<int:pk>'  ,CitaEditar.as_view(),   name  = 'cita_editar'),
    path('healthcare/atencion_medica/citas/eliminar/<int:pk>',CitaEliminar.as_view(), name  = 'cita_eliminar'),

]
