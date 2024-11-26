# registros/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PersonalCreateView, PersonalDeleteView, PersonalDetailView, PersonalListView, PersonalUpdateView, ResidenteListView, ResidenteDetailView, ResidenteCreateView, ResidenteUpdateView, ResidenteDeleteView,
    VisitanteListView, VisitanteDetailView, VisitanteCreateView, VisitanteUpdateView, VisitanteDeleteView)
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/',views.home, name="home"),



    # URLs para Residente
    path('residentes/', ResidenteListView.as_view(), name='residente_list'),
    path('residentes/<int:pk>/', ResidenteDetailView.as_view(), name='residente_detail'),
    path('residentes/nuevo/', ResidenteCreateView.as_view(), name='residente_create'),
    path('residentes/<int:pk>/editar/', ResidenteUpdateView.as_view(), name='residente_update'),
    path('residentes/<int:pk>/eliminar/', ResidenteDeleteView.as_view(), name='residente_delete'),

    # URLs para Visitante
    path('visitantes/', VisitanteListView.as_view(), name='visitante_list'),
    path('visitantes/<int:pk>/', VisitanteDetailView.as_view(), name='visitante_detail'),
    path('visitantes/nuevo/', VisitanteCreateView.as_view(), name='visitante_create'),
    path('visitantes/<int:pk>/editar/', VisitanteUpdateView.as_view(), name='visitante_update'),
    path('visitantes/<int:pk>/eliminar/', VisitanteDeleteView.as_view(), name='visitante_delete'),

    # URLs para Personal
    path('personal/', PersonalListView.as_view(), name='personal_list'),
    path('personal/<int:pk>/', PersonalDetailView.as_view(), name='personal_detail'),
    path('personal/nuevo/', PersonalCreateView.as_view(), name='personal_create'),
    path('personal/editar/<int:pk>/', PersonalUpdateView.as_view(), name='personal_update'),
    path('personal/borrar/<int:pk>/', PersonalDeleteView.as_view(), name='personal_delete'),


]
