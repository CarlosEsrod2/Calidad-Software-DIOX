# registros/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Personal, Residente, Visitante
from .forms import ResidenteForm, VisitanteForm, PersonalForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, 'registration/login.html')

# Vistas para Residente
class ResidenteListView(ListView):
    model = Residente
    template_name = 'registros/residente_list.html'  # Plantilla de lista

class ResidenteDetailView(DetailView):
    model = Residente
    template_name = 'registros/residente_detail.html'  # Plantilla de detalle

class ResidenteCreateView(CreateView):
    model = Residente
    form_class = ResidenteForm
    template_name = 'registros/residente_form.html'  # Plantilla de creación
    success_url = reverse_lazy('residente_list')  # Redirecciona a la lista después de crear

class ResidenteUpdateView(UpdateView):
    model = Residente
    form_class = ResidenteForm
    template_name = 'registros/residente_form.html'  # Plantilla de edición
    success_url = reverse_lazy('residente_list')

class ResidenteDeleteView(DeleteView):
    model = Residente
    template_name = 'registros/residente_confirm_delete.html'  # Plantilla de confirmación de borrado
    success_url = reverse_lazy('residente_list')

# Vistas para Visitante
class VisitanteListView(ListView):
    model = Visitante
    template_name = 'registros/visitante_list.html'

class VisitanteDetailView(DetailView):
    model = Visitante
    template_name = 'registros/visitante_detail.html'

class VisitanteCreateView(CreateView):
    model = Visitante
    form_class = VisitanteForm
    template_name = 'registros/visitante_form.html'
    success_url = reverse_lazy('visitante_list')

class VisitanteUpdateView(UpdateView):
    model = Visitante
    form_class = VisitanteForm
    template_name = 'registros/visitante_form.html'
    success_url = reverse_lazy('visitante_list')

class VisitanteDeleteView(DeleteView):
    model = Visitante
    template_name = 'registros/visitante_confirm_delete.html'
    success_url = reverse_lazy('visitante_list')

# Vistas para personal
class PersonalListView(ListView):
    model = Personal
    template_name = 'registros/personal_list.html'  # Plantilla de lista

class PersonalDetailView(DetailView):
    model = Personal
    template_name = 'registros/personal_detail.html'  # Plantilla de detalle

class PersonalCreateView(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'registros/personal_form.html'  # Plantilla de creación
    success_url = reverse_lazy('personal_list')  # Redirecciona a la lista después de crear

class PersonalUpdateView(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'registros/personal_form.html'  # Plantilla de edición
    success_url = reverse_lazy('personal_list')

class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = 'registros/personal_confirm_delete.html'  # Plantilla de confirmación de borrado
    success_url = reverse_lazy('personal_list')