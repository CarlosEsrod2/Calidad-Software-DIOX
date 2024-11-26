# forms.py
from django import forms
from registros.utils import verificar_rut
from .models import Personal, Residente, Visitante

class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = '__all__'

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not verificar_rut(rut):
            raise forms.ValidationError("El RUT ingresado es inválido.")
        return rut

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = '__all__'

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not verificar_rut(rut):
            raise forms.ValidationError("El RUT ingresado es inválido.")
        return rut

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not verificar_rut(rut):
            raise forms.ValidationError("El RUT ingresado es inválido.")
        return rut