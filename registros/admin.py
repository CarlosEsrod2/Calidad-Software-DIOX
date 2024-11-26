# registros/admin.py
from django.contrib import admin
from .models import Residente, Visitante

admin.site.register(Residente)
admin.site.register(Visitante)
