from rest_framework import serializers
from .models import DonneeCapteur, UserDispositif, User, Dispositif


class DonneeCapteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeCapteur
        fields = '__all__'
        
class DonneeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class DonneeDispositifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositif
        fields = '__all__'
        
class DonneeUserDispositifSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDispositif
        fields = '__all__'
