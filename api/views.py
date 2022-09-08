from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomerDataRegistration
from api.serializers import CustomerDataRegistrationSerializer


@api_view(['GET'])
def get_customers(request):
    customers = CustomerDataRegistration.objects.all()
    serializer = CustomerDataRegistrationSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_customers(request):
    serializer = CustomerDataRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
