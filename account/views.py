from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserDispositifForm
from .models import Dispositif, UserDispositif, DonneeCapteur, User
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DonneeCapteurSerializer, DonneeUserDispositifSerializer, DonneeUserSerializer, DonneeDispositifSerializer
from django.http import JsonResponse
from rest_framework.views import APIView

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


"""
@login_required
def ajouter_dispositif(request, id_dispositif):
    dispositif = get_object_or_404(Dispositif, pk=id_dispositif)
    request.user.dispositifs.add(dispositif)
    return redirect('confirmation_dispositif')
"""


def confirmation_dispositif(request):
    return render(request, 'account/confirmation_dispositif.html')

"""
@login_required
def mes_dispositifs(request):
    dispositifs = request.user.dispositifs.all()
    return render(request, 'account/mes_dispositifs.html', {'dispositifs': dispositifs})
"""

@login_required
def mes_dispositifs(request):
    user_dispositifs = UserDispositif.objects.filter(user=request.user)
    return render(request, 'account/mes_dispositifs.html', {'user_dispositifs': user_dispositifs})

"""
@login_required
def ajouter_dispositif(request, id_dispositif):
    dispositif = get_object_or_404(Dispositif, pk=id_dispositif)
    user_dispositif, created = UserDispositif.objects.get_or_create(
        user=request.user, 
        dispositif=dispositif
    )
    if created:
        user_dispositif.save()
    return redirect('confirmation_dispositif')
    """
    
@login_required
def ajouter_dispositif(request, id_dispositif):
    dispositif = get_object_or_404(Dispositif, pk=id_dispositif)
    user_dispositif = UserDispositif(user=request.user, dispositif=dispositif)
    user_dispositif.save()
    return redirect('confirmation_dispositif')

@login_required
def supprimer_dispositif(request, user_dispositif_id):
    user_dispositif = get_object_or_404(UserDispositif, pk=user_dispositif_id, user=request.user)
    user_dispositif.delete()
    return redirect('liste_dispositifs_utilisateur')


@login_required
def modifier_dispositif(request, user_dispositif_id):
    user_dispositif = get_object_or_404(UserDispositif, pk=user_dispositif_id, user=request.user)

    if request.method == 'POST':
        form = UserDispositifForm(request.POST, instance=user_dispositif)
        if form.is_valid():
            form.save()
            return redirect('liste_dispositifs_utilisateur')
    else:
        form = UserDispositifForm(instance=user_dispositif)

    return render(request, 'account/modifier_dispositif.html', {'form': form})



@api_view(['POST'])
def recevoir_donnee(request):
    # Identification des dispositifs
    code_dispositif = request.data.get('code_dispositif')
    user_dispositif = UserDispositif.objects.filter(code=code_dispositif).first()

    if user_dispositif is None:
        return Response({'error': 'Dispositif non trouvé'}, status=404)

    serializer = DonneeCapteurSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(user_dispositif=user_dispositif)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    return JsonResponse({'status': 'success'})

class DonneeCapteurList(APIView):
    def get(self, request, format=None):
        donnees = DonneeCapteur.objects.all()
        serializer = DonneeCapteurSerializer(donnees, many=True)
        return Response(serializer.data)
    
class DonneeUserList(APIView):
    def get(self, request, format=None):
        donnees = User.objects.all()
        serializer = DonneeUserSerializer(donnees, many=True)
        return Response(serializer.data)
    
class DonneeDispositifList(APIView):
    def get(self, request, format=None):
        donnees = Dispositif.objects.all()
        serializer = DonneeDispositifSerializer(donnees, many=True)
        return Response(serializer.data)

class DonneeUserDispositifList(APIView):
    def get(self, request, format=None):
        donnees = UserDispositif.objects.all()
        serializer = DonneeUserDispositifSerializer(donnees, many=True)
        return Response(serializer.data)
    
@login_required
def visualiser_capteur(request, user_dispositif_id):
    user_dispositif = get_object_or_404(UserDispositif, pk=user_dispositif_id, user=request.user)
    donnees = DonneeCapteur.objects.filter(user_dispositif=user_dispositif).order_by('-date_heure')[:20]

    context = {
        'user_dispositif': user_dispositif,
        'donnees': donnees
    }
    return render(request, 'account/visualiser_capteur.html', context)





   












