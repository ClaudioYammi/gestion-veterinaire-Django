# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient, Proprietaire, Veterinaire, Rendezvous, Traitement 
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import DateField, TimeField
from django.forms import DateInput, TimeInput

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.core.paginator import Paginator


@login_required
def home(request):
    total_patient            =Patient.objects.count()
    total_proprietaire       =Proprietaire.objects.count()
    total_traitement         =Traitement.objects.count()
    total_rendezvous         =Rendezvous.objects.count()
    total_veterinaire        =Veterinaire.objects.count()
    context = {
        'total_patient'      :total_patient,
        'total_proprietaire' :total_proprietaire,
        'total_traitement'   :total_traitement,
        'total_veterinaire'  :total_veterinaire,
        'total_rendezvous'  :total_rendezvous
    }

    return render(request, "Dashboard/index.html", context)

# def login_view(request):
#     invalid_credentials = False
#     if request.method == 'POST':
#         # Vérifier les informations d'identification
#         if credentials_are_invalid:
#             invalid_credentials = True
#         else:
#             # Connexion réussie, effectuer les actions nécessaires
#             return redirect('Dashboard/index.html')
    
#     context = {
#         'invalid_credentials': invalid_credentials
#     }
#     return render(request, 'Patient/form.html', context)

# Create your views Patient ------------------------------------------------------------------------------------- #
class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "Patient/list.html"
    context_object_name="patients" # list tableau
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')
        patients = paginator.get_page(page)
        context['patients'] = patients
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nom_pa__icontains=search_query)|
                Q(espece__icontains=search_query)|
                Q(race__icontains=search_query)|
                Q(age__icontains=search_query)|
                Q(antecedants_medicaux__icontains=search_query)|
                Q(sexe__icontains=search_query)
            )
        return queryset
    
    # def patient_list(request):
    #     patients = Patient.objects.all()
    #     paginator = Paginator(patients, 10)  # Divise les patients en pages de 10 éléments par page

    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)

    #     return render(request, 'patient_list.html', {'page_obj': page_obj})
    
    
        

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['nom_pa', 'espece', 'race', 'age', 'antecedants_medicaux', 'sexe']
    success_url = reverse_lazy('patient-list')
    template_name = "Patient/form.html"

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['nom_pa', 'espece', 'race', 'age', 'antecedants_medicaux', 'sexe']
    success_url = reverse_lazy('patient-list')
    template_name = "Patient/form.html"

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patient-list')
    template_name = "Patient/confirm_delete.html"

# Create your views Proprietaire  ------------------------------------------------------------------------------------- #
class ProprietaireListView(LoginRequiredMixin,ListView):
    model = Proprietaire
    template_name = "Proprietaire/list.html"
    context_object_name="proprietaires" # list tableau

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nom_pro__icontains=search_query)|
                Q(prenom__icontains=search_query)|
                Q(adresse__icontains=search_query)|
                Q(email__icontains=search_query)|
                Q(sexe__icontains=search_query)
            )
        return queryset

class ProprietaireCreateView(LoginRequiredMixin,CreateView):
    model = Proprietaire
    fields = ['nom_pro', 'prenom', 'adresse', 'email', 'telephone', 'sexe', 'patient']
    success_url = reverse_lazy('proprietaire-list')
    template_name = "Proprietaire/form.html"

class ProprietaireUpdateView(LoginRequiredMixin,UpdateView):
    model = Proprietaire
    fields = ['nom_pro', 'prenom', 'adresse', 'email', 'telephone', 'sexe', 'patient']
    success_url = reverse_lazy('proprietaire-list')
    template_name = "Proprietaire/form.html"

class ProprietaireDeleteView(LoginRequiredMixin,DeleteView):
    model = Proprietaire
    success_url = reverse_lazy('proprietaire-list')
    template_name = "Proprietaire/confirm_delete.html"


# Create your views Veterinaire  ------------------------------------------------------------------------------------- #
class VeterinaireListView(LoginRequiredMixin,ListView):
    model = Veterinaire
    template_name = "Veterinaire/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nom_ve__icontains=search_query)|
                Q(prenom__icontains=search_query)|
                Q(specialiter__icontains=search_query)|
                Q(adresse__icontains=search_query)|
                Q(email=search_query)|
                Q(sexe__icontains=search_query)
            )
        return queryset

class VeterinaireCreateView(LoginRequiredMixin,CreateView):
    model = Veterinaire
    fields = ['nom_ve', 'prenom', 'specialiter','adresse', 'email', 'telephone', 'sexe', 'specialiter']
    success_url = reverse_lazy('veterinaire-list')
    template_name = "Veterinaire/form.html"

class VeterinaireUpdateView(LoginRequiredMixin,UpdateView):
    model = Veterinaire
    fields = ['nom_ve', 'prenom', 'specialiter', 'adresse', 'email', 'telephone', 'sexe', 'specialiter']
    success_url = reverse_lazy('veterinaire-list')
    template_name = "Veterinaire/form.html"

class VeterinaireDeleteView(LoginRequiredMixin,DeleteView):
    model = Veterinaire
    success_url = reverse_lazy('veterinaire-list')
    template_name = "Veterinaire/confirm_delete.html"

# Create your views Traitement  ------------------------------------------------------------------------------------- #

class TraitementListView(LoginRequiredMixin,ListView):
    model = Traitement
    template_name = "Traitement/list.html"
    context_object_name="traitements" # list tableau

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(date_traitement__icontains=search_query)|
                Q(medicament__icontains=search_query)|
                Q(dosages__icontains=search_query)|
                Q(instructions__icontains=search_query)
            )
        return queryset

class TraitementCreateView(LoginRequiredMixin,CreateView):
    model = Traitement
    fields = ['date_traitement', 'medicament', 'dosages', 'instructions', 'patient', 'veterinaire']
    success_url = reverse_lazy('traitement-list')
    template_name = "Traitement/form.html"

class TraitementUpdateView(LoginRequiredMixin,UpdateView):
    model = Traitement
    fields = ['date_traitement', 'medicament', 'dosages', 'instructions', 'patient', 'veterinaire']
    success_url = reverse_lazy('traitement-list')
    template_name = "Traitement/form.html"

class TraitementDeleteView(LoginRequiredMixin,DeleteView):
    model = Traitement
    success_url = reverse_lazy('traitement-list')
    template_name = "Traitement/confirm_delete.html"

# Create your views Rendezvous  ------------------------------------------------------------------------------------- #

class RendezVousListView(LoginRequiredMixin,ListView):
    model = Rendezvous
    template_name = "Rendezvous/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(motif__icontains=search_query)|
                Q(observation__icontains=search_query)|
                Q(date__icontains=search_query)|
                Q(heure__icontains=search_query)|
                Q(patient__icontains=search_query)|
                Q(veterinaire__icontains=search_query)
            )
        return queryset

class RendezVousCreateView(LoginRequiredMixin,CreateView):
    model = Rendezvous
    fields = ['motif', 'observation', 'date', 'heure', 'patient', 'veterinaire']
    success_url = reverse_lazy('rendezvous-list')
    template_name = "Rendezvous/form.html"
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'] = DateField(widget=DateInput(attrs={'type': 'date'}))
        form.fields['heure'] = TimeField(widget=TimeInput(attrs={'type': 'time'}))
        return form


class RendezVousUpdateView(LoginRequiredMixin,UpdateView):
    model = Rendezvous
    fields = ['motif', 'observation', 'date', 'heure', 'patient', 'veterinaire']
    success_url = reverse_lazy('rendezvous-list')
    template_name = "Rendezvous/form.html"
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'] = DateField(widget=DateInput(attrs={'type': 'date'}))
        form.fields['heure'] = TimeField(widget=TimeInput(attrs={'type': 'time'}))
        return form

class RendezVousDeleteView(LoginRequiredMixin,DeleteView):
    model = Rendezvous
    success_url = reverse_lazy('rendezvous-list')
    template_name = "Rendezvous/confirm_delete.html"

# Pagination ---------------------------------
