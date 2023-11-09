from django.urls import path
from .views import home, services, about, contact, register, login

urlpatterns = [

    path('',home, name='Acceuil' ),
    path('Services/',services, name='Services' ),
    path('A_porpos/',about, name='A_propos' ),
    path('Contact/',contact, name='Contact' ),
    path('Register/',register, name='Register' ),
    path('Login/',login, name='Login' ),
]
