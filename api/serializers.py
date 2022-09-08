from rest_framework import serializers
from accounts.models import CustomerDataRegistration


class CustomerDataRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDataRegistration
        fields = '__all__'
