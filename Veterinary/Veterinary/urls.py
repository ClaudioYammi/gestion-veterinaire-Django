
"""
URL configuration for Veterinary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_patient.views import (
    home,
    ProprietaireListView, ProprietaireCreateView, ProprietaireUpdateView, ProprietaireDeleteView,
    PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView,
    RendezVousListView, RendezVousCreateView, RendezVousUpdateView, RendezVousDeleteView,
    VeterinaireListView, VeterinaireCreateView, VeterinaireUpdateView, VeterinaireDeleteView,
    TraitementListView, TraitementCreateView, TraitementUpdateView, TraitementDeleteView
)

from django.contrib.auth.views import LoginView, LogoutView
# from app_patient.views import MonLoginView, MonLogoutView, MonInscriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs pour Proprietaire
    path('home/', home, name='home'),

    # URLs pour Proprietaire
    path('login/', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    path('logout/', LogoutView.as_view(
        next_page="login"
    ), name='logout'),

    # URLs pour Proprietaire
    path('proprietaire/', ProprietaireListView.as_view(), name='proprietaire-list'),
    path('proprietaire/create/', ProprietaireCreateView.as_view(), name='proprietaire-create'),
    path('proprietaire/<int:pk>/update/', ProprietaireUpdateView.as_view(), name='proprietaire-update'),
    path('proprietaire/<int:pk>/delete/', ProprietaireDeleteView.as_view(), name='proprietaire-delete'),
    
    # URLs pour Patient
    path('patient/', PatientListView.as_view(), name='patient-list'),
    path('patient/create/', PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
    
    # URLs pour Rendez-vous
    path('rendezvous/', RendezVousListView.as_view(), name='rendezvous-list'),
    path('rendezvous/create/', RendezVousCreateView.as_view(), name='rendezvous-create'),
    path('rendezvous/<int:pk>/update/', RendezVousUpdateView.as_view(), name='rendezvous-update'),
    path('rendezvous/<int:pk>/delete/', RendezVousDeleteView.as_view(), name='rendezvous-delete'),
    
    # URLs pour Veterinaire
    path('veterinaire/', VeterinaireListView.as_view(), name='veterinaire-list'),
    path('veterinaire/create/', VeterinaireCreateView.as_view(), name='veterinaire-create'),
    path('veterinaire/<int:pk>/update/', VeterinaireUpdateView.as_view(), name='veterinaire-update'),
    path('veterinaire/<int:pk>/delete/', VeterinaireDeleteView.as_view(), name='veterinaire-delete'),

    # URLs pour Traitement
    path('traitement/', TraitementListView.as_view(), name='traitement-list'),
    path('traitement/create/', TraitementCreateView.as_view(), name='traitement-create'),
    path('traitement/<int:pk>/update/', TraitementUpdateView.as_view(), name='traitement-update'),
    path('traitement/<int:pk>/delete/', TraitementDeleteView.as_view(), name='traitement-delete'),
]