# test_models.py
import pytest
from django.core.exceptions import ValidationError
from ..models import Residente, Visitante, Personal
from ..utils import verificar_rut  # Asegúrate de que esta función exista

@pytest.mark.django_db
class TestResidenteModel:
    
    def test_registro_residente_rut_invalido(self):
        residente = Residente(rut='12345678-9', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            residente.full_clean()

    def test_registro_residente_nombre_vacio(self):
        residente = Residente(rut='23940081-7', nombre='', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            residente.full_clean()

    def test_registro_residente_apellido_vacio(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            residente.full_clean()

    def test_registro_residente_sin_alergias(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', alergias_medicamentos=None)
        residente.full_clean()

    def test_registro_residente_fecha_nacimiento_futura(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='3000-01-01')
        residente.full_clean()

    def test_registro_residente_sin_contacto_emergencia(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', contactos_emergencia=None)
        residente.full_clean()

    def test_registro_residente_preferencias_alimentarias_vacias(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', preferencias_alimentarias=None)
        residente.full_clean()

    def test_registro_residente_enfermedades_cronicas_vacias(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', enfermedades_cronicas=None)
        residente.full_clean()

    def test_registro_residente_historial_accidentes_extenso(self):
        extenso_historial = 'A' * 1001  # Asumiendo que el límite es de 1000 caracteres
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', historial_accidentes=extenso_historial)
        residente.full_clean()

    def test_registro_residente_informacion_tutor_incompleta(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', apoderado_tutor=None)
        residente.full_clean()

    def test_registro_residente_exitoso(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', contactos_emergencia='123456789', alergias_medicamentos='Ninguna')
        residente.full_clean()  # No debería lanzar excepción

    def test_registro_residente_sin_huella_dactilar(self):
        residente = Residente(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01', huella_dactilar=None)
        residente.full_clean()  # No debería lanzar excepción

    def test_validacion_rut_duplicado(self):
        Residente.objects.create(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01')
        residente_duplicado = Residente(rut='23940081-7', nombre='Pedro', apellido_paterno='Gómez', fecha_nacimiento='1990-01-01')
        with pytest.raises(ValidationError):
            residente_duplicado.full_clean()

    def test_modificacion_informacion_residente(self):
        residente = Residente.objects.create(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', fecha_nacimiento='2000-01-01')
        residente.nombre = 'Carlos'
        residente.full_clean()  # No debería lanzar excepción


@pytest.mark.django_db
class TestVisitanteModel:

    def test_registro_visitante_sin_rut(self):
        visitante = Visitante(rut='', nombre='Juan', apellido_paterno='Pérez', parentesco_residente='Hijo', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            visitante.full_clean()

    def test_registro_visitante_rut_invalido(self):
        visitante = Visitante(rut='12345678-9', nombre='Juan', apellido_paterno='Pérez', parentesco_residente='Hijo', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            visitante.full_clean()

    def test_registro_visitante_sin_nombre(self):
        visitante = Visitante(rut='23940081-7', nombre='', apellido_paterno='Pérez', parentesco_residente='Hijo', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            visitante.full_clean()

    def test_registro_visitante_sin_parentesco(self):
        visitante = Visitante(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', parentesco_residente='', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            visitante.full_clean()

    def test_registro_visitante_apellido_paterno_vacio(self):
        visitante = Visitante(rut='23940081-7', nombre='Juan', apellido_paterno='', parentesco_residente='Hijo', fecha_nacimiento='2000-01-01')
        with pytest.raises(ValidationError):
            visitante.full_clean()

    def test_registro_visitante_fecha_nacimiento_invalida(self):
        visitante = Visitante(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', parentesco_residente='Hijo', fecha_nacimiento='3000-01-01')
        visitante.full_clean()

    def test_registro_visitante_sin_huella_dactilar(self):
        visitante = Visitante(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', parentesco_residente='Hijo', fecha_nacimiento='2000-01-01', huella_dactilar=None)
        visitante.full_clean()  # No debería lanzar excepción

    def test_registro_visitante_rut_duplicado(self):
        Visitante.objects.create(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', parentesco_residente='Hijo', fecha_nacimiento='2000-01-01')
        visitante_duplicado = Visitante(rut='23940081-7', nombre='Pedro', apellido_paterno='Gómez', parentesco_residente='Hermano', fecha_nacimiento='1995-01-01')
        with pytest.raises(ValidationError):
            visitante_duplicado.full_clean()

    def test_registro_visitante_exitoso(self):
        visitante = Visitante(rut='23940081-7', nombre='Juan', apellido_paterno='Pérez', parentesco_residente='Hijo', fecha_nacimiento='2000-01-01')
        visitante.full_clean()  # No debería lanzar excepción


@pytest.mark.django_db
class TestPersonalModel:

    def test_registro_personal_sin_rut(self):
        personal = Personal(rut='', primer_nombre='Carlos', apellido_paterno='Pérez', cargo='Enfermero', turno='Mañana')
        with pytest.raises(ValidationError):
            personal.full_clean()

    def test_registro_personal_rut_invalido(self):
        personal = Personal(rut='12345678-9', primer_nombre='Carlos', apellido_paterno='Pérez', cargo='Enfermero', turno='Mañana')
        with pytest.raises(ValidationError):
            personal.full_clean()

    def test_registro_personal_sin_nombre(self):
        personal = Personal(rut='23940081-7', primer_nombre='', apellido_paterno='Pérez', cargo='Enfermero', turno='Mañana')
        with pytest.raises(ValidationError):
            personal.full_clean()

    def test_registro_personal_sin_apellido_paterno(self):
        personal = Personal(rut='23940081-7', primer_nombre='Carlos', apellido_paterno='', cargo='Enfermero', turno='Mañana')
        with pytest.raises(ValidationError):
            personal.full_clean()

    def test_registro_personal_sin_cargo(self):
        personal = Personal(rut='23940081-7', primer_nombre='Carlos', apellido_paterno='Pérez', cargo='', turno='Mañana')
        with pytest.raises(ValidationError):
            personal.full_clean()

    def test_registro_personal_sin_turno(self):
        personal = Personal(rut='23940081-7', primer_nombre='Carlos', apellido_paterno='Pérez', cargo='Enfermero', turno='')
        with pytest.raises(ValidationError):
            personal.full_clean()

    def test_registro_personal_sin_pacientes_asignados(self):
        personal = Personal(rut='23940081-7', primer_nombre='Carlos', apellido_paterno='Pérez', cargo='Enfermero', turno='Mañana', pacientes_asignados=None)
        personal.full_clean()

    def test_registro_personal_rut_duplicado(self):
        Personal.objects.create(rut='23940081-7', primer_nombre='Carlos', apellido_paterno='Pérez', cargo='Enfermero', turno='Mañana')
        personal_duplicado = Personal(rut='23940081-7', primer_nombre='Ana', apellido_paterno='Gómez', cargo='Doctor', turno='Tarde')
        with pytest.raises(ValidationError):
            personal_duplicado.full_clean()

    def test_registro_personal_exitoso(self):
        personal = Personal(rut='23940081-7', primer_nombre='Carlos', apellido_paterno='Pérez', cargo='Enfermero', turno='Mañana', pacientes_asignados='Paciente 1')
        personal.full_clean()  # No debería lanzar excepción
