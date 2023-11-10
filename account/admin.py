from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Importez votre modèle utilisateur personnalisé

# Enregistrez votre modèle utilisateur avec l'interface d'administration
admin.site.register(User, UserAdmin)
