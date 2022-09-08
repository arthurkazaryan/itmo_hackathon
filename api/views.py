from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomerDataRegistration, LocationCamera, Profile
from api.serializers import CustomerDataRegistrationSerializer
from tgbot.misc import send_warning_message


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
        if serializer.data['warning_flag']:
            camera_object = LocationCamera.objects.filter(id=serializer.data['camera'])
            if camera_object:
                user_profile = Profile.objects.filter(user=camera_object[0].user)
                if user_profile:
                    telegram_chat_id = user_profile[0].chat_id
                    send_warning_message(telegram_chat_id, 'В вашем магазине дофига очередь. Пните кассиров.')
    return Response(serializer.data)
