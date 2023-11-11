from rest_framework import serializers
from .models import DonneeCapteur


class DonneeCapteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeCapteur
        fields = '__all__'
