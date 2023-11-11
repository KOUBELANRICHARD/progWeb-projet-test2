from django.urls import path
from .views import home, services, about, contact, register, login
from account.views import SignUpView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',home, name='Acceuil' ),
    path('Services/',services, name='Services' ),
    path('A_porpos/',about, name='A_propos' ),
    path('Contact/',contact, name='Contact' ),
    path('Register/',SignUpView.as_view(), name='Register' ),
    path('Login/', CustomLoginView.as_view(), name='Login'),
    path('Logout/', LogoutView.as_view(), name='Logout'),
   
]
