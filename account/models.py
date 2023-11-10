from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    adresse = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email

from django.db import models
import random
import string

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
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dispositifs')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        super(Dispositif, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom
    

