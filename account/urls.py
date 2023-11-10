from django.urls import path
from .views import home_customer, devices, collectes, commandes

urlpatterns = [

    path('',home_customer, name='Home' ),
    path('Device/',devices, name='Devices' ),
    path('Collecte/',collectes, name='Collectes' ),
    path('Commande/',commandes, name='Commandes' ),
   
]