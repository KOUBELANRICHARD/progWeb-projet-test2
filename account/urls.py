from django.urls import path
from .views import home_customer, devices, collectes, commandes, liste_dispositifs, ajouter_dispositif, confirmation_dispositif, mes_dispositifs, supprimer_dispositif, modifier_dispositif, visualiser_capteur
from .views import recevoir_donnee, DonneeCapteurList, DonneeUserList, DonneeDispositifList, DonneeUserDispositifList

urlpatterns = [

    path('',liste_dispositifs, name='Home' ),
    path('Device/',devices, name='Devices' ),
    path('Collecte/',collectes, name='Collectes' ),
    path('Commande/',commandes, name='Commandes' ),
    path('ajouter-dispositif/<int:id_dispositif>/', ajouter_dispositif, name='ajouter_dispositif'),
    path('confirmation_dispositif', confirmation_dispositif, name='confirmation_dispositif'),
    path('customer_dispositif', mes_dispositifs, name='liste_dispositifs_utilisateur'),
    path('visualiser-capteur/<int:user_dispositif_id>/', visualiser_capteur, name='visualiser_capteur'),
    path('modifier-dispositif/<int:user_dispositif_id>/', modifier_dispositif, name='modifier_dispositif'),
    path('supprimer-dispositif/<int:user_dispositif_id>/', supprimer_dispositif, name='supprimer_dispositif'),
    path('api/recevoir-donnee/', recevoir_donnee, name='recevoir_donnee'),
    path('api/donnees-clients/', DonneeUserList.as_view(), name='donnee-user-list'),
    path('api/donnees-dispositifs/', DonneeDispositifList.as_view(), name='donnee-dispositif-list'),
    path('api/donnees-user-dispositifs/', DonneeUserDispositifList.as_view(), name='donnee-dispositif-list'),
    path('api/donnees/', DonneeCapteurList.as_view(), name='donnee-capteur-list'),
]
    
   
