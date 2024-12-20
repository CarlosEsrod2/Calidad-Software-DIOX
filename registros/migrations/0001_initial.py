# Generated by Django 5.0.6 on 2024-10-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('apoderado_tutor', models.CharField(blank=True, max_length=100, null=True)),
                ('alergias_medicamentos', models.TextField(blank=True, null=True)),
                ('alergias_alimentarias', models.TextField(blank=True, null=True)),
                ('enfermedades_cronicas', models.TextField(blank=True, null=True)),
                ('medicamentos', models.TextField(blank=True, null=True)),
                ('contactos_emergencia', models.TextField(blank=True, null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=20, null=True)),
                ('nivel_autonomia', models.CharField(blank=True, max_length=50, null=True)),
                ('preferencias_alimentarias', models.TextField(blank=True, null=True)),
                ('historial_accidentes', models.TextField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('huella_dactilar', models.BinaryField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('parentesco_residente', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('huella_dactilar', models.BinaryField(blank=True, null=True)),
            ],
        ),
    ]
