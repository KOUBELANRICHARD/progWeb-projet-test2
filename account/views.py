from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Dispositif

# Vues basées sur des fonctions avec login_required
@login_required(login_url='/Login/')
def home_customer(request):
    return render(request, 'account/index.html')

@login_required(login_url='/Login/')
def devices(request):
    return render(request, 'account/services.html')

@login_required(login_url='/Login/')
def collectes(request):
    return render(request, 'account/about.html')

@login_required(login_url='/Login/')
def commandes(request):
    return render(request, 'account/contact.html')

# Vues basées sur des classes
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Home')
    template_name = 'blog/register.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('Home')
    template_name = 'blog/login.html'
    

@login_required(login_url='/Login/')
def liste_dispositifs(request):
    dispositifs = Dispositif.objects.all()
    return render(request, 'account/index.html', {'dispositifs': dispositifs})







