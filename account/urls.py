from django.urls import path
from .views import home_customer, devices, collectes, commandes, liste_dispositifs

urlpatterns = [

    path('',liste_dispositifs, name='Home' ),
    path('Device/',devices, name='Devices' ),
    path('Collecte/',collectes, name='Collectes' ),
    path('Commande/',commandes, name='Commandes' ),
   
]