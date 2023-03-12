from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


from .serializers import RegistrationSerializer

@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = get_user_model().objects.create_user(
                request.data['email'],
                request.data['name'],
                request.data['password']
            )
            data['user'] = user.id
            data['email'] = request.data['email']
            data['name'] = request.data['name']
            data['token'] = Token.objects.get(user=user).key
        else:
            data = serializer.errors
        return Response(data)