from django.db import models

# Create your models here.

class Departamento(models.Model):
    NoDepto        = models.AutoField(primary_key=True)
    Especialidad   = models.CharField(max_length=100)
    concentracion  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.NoDepto)+ ' '+self.Especialidad

class Consultorio(models.Model):
    NoConsultorio  = models.AutoField(primary_key=True)
    Jornada        = models.CharField(max_length=70)
    Piso           = models.IntegerField()
    NoDepto        = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return str(self.NoConsultorio)+ ' -Depto: '+str(self.NoDepto)

class Doctor(models.Model):
    IdDoctor      = models.AutoField(primary_key=True)
    Nombres       = models.CharField(max_length=100)
    Apellidos     = models.CharField(max_length=100)
    FechaNac      = models.DateField()
    Telefono      = models.CharField(max_length=8)
    correo        = models.CharField(max_length=254)
    FechaIngreso  = models.DateField()
    NoConsultorio = models.ForeignKey(Consultorio, on_delete=models.PROTECT, null=False, blank=False)
    def __str__(self):
        return str(self.IdDoctor)+ ' '+self.Nombres

class Paciente(models.Model):
    DNI           = models.CharField(max_length=13,primary_key=True)
    Nombres       = models.CharField(max_length=100)
    Apellidos     = models.CharField(max_length=100)
    FechaNac      = models.DateField()
    Telefono      = models.CharField(max_length=8)
    correo        = models.CharField(max_length=254)
    Direccion     = models.CharField(max_length=200)
    def __str__(self):
        return str(self.DNI)+ ' '+self.Nombres

class Cita(models.Model):
    NoCita        = models.AutoField(primary_key=True)
    FechaRegistro = models.DateField()
    FechaAtencion = models.DateTimeField()
    DniPaciente   = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=False, blank=False)
    IdDoctor      = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=False, blank=False)
    Descripcion   = models.CharField(max_length=200)
    def __str__(self):
        return str(self.NoCita)+ ' '+str(self.DniPaciente)