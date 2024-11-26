# residencia_ancianos/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('registros/', include('registros.urls')),  # Incluye las URLs de la app registros
]
