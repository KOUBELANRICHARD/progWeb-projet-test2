from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Dispositif

# Enregistrez votre modèle utilisateur avec l'interface d'administration
admin.site.register(User, UserAdmin)

@admin.register(Dispositif)
class DispositifAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'description', 'localisation', 'code')

