from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .permissions import AdminPermission, SuperstudentPermission

from .serializers import RegistrationSerializer, RoleAssignmentSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
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

@api_view(['POST'])
@permission_classes([AdminPermission|SuperstudentPermission])
def role_assignment_view(request):
    if request.method == "POST":
        serializer = RoleAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            user = get_user_model().objects.get(email=request.data['email'])

            if not user:
                return ValueError()

            user.role = request.data['role']
            user.save()
            data = {'message': f'{user.email} is nu een {request.data.group}'}
        else:
            data = serializer.errors
        return Response(data)
