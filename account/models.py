from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import random
import string
from datetime import datetime


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    adresse = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email


class Dispositif(models.Model):
    # Définissez vos choix comme des constantes de classe
    TYPE_CAPTEUR = 'CAPTEUR'
    TYPE_ACTUATEUR = 'ACTUATEUR'
    TYPE_CHOICES = (
        (TYPE_CAPTEUR, 'Capteur'),
        (TYPE_ACTUATEUR, 'Actuateur'),
    )
    
    id_dispositif = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=200,choices=TYPE_CHOICES,default=TYPE_CAPTEUR)
    image = models.ImageField(upload_to='images/')  # Configuration des medias
    description = models.TextField()
    localisation = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=4, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        super(Dispositif, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom
    

class UserDispositif(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dispositif = models.ForeignKey(Dispositif, on_delete=models.CASCADE)
    code = models.CharField(max_length=4, blank=True)
    localisation = models.CharField(max_length=200, blank=True)  # Ajout du champ localisation
        
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        super(UserDispositif, self).save(*args, **kwargs)
        
class DonneeCapteur(models.Model):
    user_dispositif = models.ForeignKey(UserDispositif, on_delete=models.CASCADE)
    valeur = models.FloatField()
    date_heure = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user_dispositif.dispositif.nom} - {self.date_heure}"

