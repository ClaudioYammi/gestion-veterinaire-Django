from django.db import models
from django.contrib import admin


# Create your models here.
class Patient(models.Model):
    nom_pa=models.CharField(max_length=50)
    espece=models.CharField(max_length=50)
    race=models.CharField(max_length=50)
    age=models.IntegerField()
    CHOICE_SEXE = [
        ('male', "male"),
        ('femelle', "femelle"),
    ]
    antecedants_medicaux=models.CharField(max_length=50)
    sexe=models.CharField(choices=CHOICE_SEXE, max_length=20)
    
    def __str__(self) -> str:
        return f"{self.nom_pa}"
    
class Proprietaire(models.Model):
    nom_pro=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    telephone=models.IntegerField()
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="prop_patient",default="")
    CHOICE_SEXE = [
        ("homme", "Homme"),
        ("femme", "Femme"),
    ]
    sexe=models.CharField(choices=CHOICE_SEXE, max_length=20)
    def _str_(self) -> str:
        return f"{self.nom_pro}"   

class Veterinaire(models.Model):
    
    nom_ve=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    specialiter=models.CharField(max_length=50, default="")
    adresse=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    telephone=models.IntegerField()
    CHOICE_SEXE = [
        ("homme", "Homme"),
        ("femme", "Femme"),
    ]
    sexe=models.CharField(choices=CHOICE_SEXE, max_length=20)
    def __str__(self) -> str:
        return f"{self.nom_ve}"  

class Traitement(models.Model):
    date_traitement=models.DateField()
    medicament=models.CharField(max_length=50)
    dosages=models.CharField(max_length=50)
    instructions=models.CharField(max_length=250)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="trai_patient")
    veterinaire=models.ForeignKey(Veterinaire, on_delete=models.CASCADE,related_name="trai_veterinaire")
    

class Rendezvous(models.Model):
    motif=models.CharField(max_length=50)
    observation=models.CharField(max_length=250)
    date=models.DateField()
    heure=models.TimeField()
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="rdv_patient")
    veterinaire=models.ForeignKey(Veterinaire, on_delete=models.CASCADE,related_name="rdv_veterinaire")

    

admin.site.register(Patient)
admin.site.register(Proprietaire)
admin.site.register(Veterinaire)
admin.site.register(Traitement)
admin.site.register(Rendezvous)