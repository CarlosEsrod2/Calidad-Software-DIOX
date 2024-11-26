from django.core.exceptions import ValidationError
from django.db import models
from .utils import verificar_rut  # Asegúrate de importar la función

class Residente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    apoderado_tutor = models.CharField(max_length=100, blank=True, null=True)
    alergias_medicamentos = models.TextField(blank=True, null=True)
    alergias_alimentarias = models.TextField(blank=True, null=True)
    enfermedades_cronicas = models.TextField(blank=True, null=True)
    medicamentos = models.TextField(blank=True, null=True)
    contactos_emergencia = models.TextField(blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    nivel_autonomia = models.CharField(max_length=50, blank=True, null=True)
    preferencias_alimentarias = models.TextField(blank=True, null=True)
    historial_accidentes = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    huella_dactilar = models.BinaryField(blank=True, null=True)

    def clean(self):
        if not verificar_rut(self.rut):
            raise ValidationError("RUT inválido.")

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class Visitante(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    parentesco_residente = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    huella_dactilar = models.BinaryField(blank=True, null=True)

    def clean(self):
        if not verificar_rut(self.rut):
            raise ValidationError("RUT inválido.")
        
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"


class Personal(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    primer_nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    turno = models.CharField(max_length=20)
    rut_paciente = models.CharField(max_length=12, blank=True, null=True)  # RUT de paciente (opcional)
    
    pacientes_asignados = models.TextField(
        blank=True, 
        help_text="Lista de RUTs separados por comas."
    )

    def clean(self):
        if not verificar_rut(self.rut):
            raise ValidationError("RUT inválido.")

    def __str__(self):
        return f"{self.primer_nombre} {self.apellido_paterno}"
