from django.urls import path
from .views import home_customer, devices, collectes, commandes, liste_dispositifs, ajouter_dispositif, confirmation_dispositif, mes_dispositifs, supprimer_dispositif, modifier_dispositif

urlpatterns = [

    path('',liste_dispositifs, name='Home' ),
    path('Device/',devices, name='Devices' ),
    path('Collecte/',collectes, name='Collectes' ),
    path('Commande/',commandes, name='Commandes' ),
    path('ajouter-dispositif/<int:id_dispositif>/', ajouter_dispositif, name='ajouter_dispositif'),
    path('confirmation_dispositif', confirmation_dispositif, name='confirmation_dispositif'),
    path('customer_dispositif', mes_dispositifs, name='liste_dispositifs_utilisateur'),
    path('modifier-dispositif/<int:user_dispositif_id>/', modifier_dispositif, name='modifier_dispositif'),
    path('supprimer-dispositif/<int:user_dispositif_id>/', supprimer_dispositif, name='supprimer_dispositif'),
    
   
]