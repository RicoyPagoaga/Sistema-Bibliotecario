from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Consultorio)
admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Cita)