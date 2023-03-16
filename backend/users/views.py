from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import serializers, generics

from django.contrib.auth import get_user_model
from .permissions import AdminPermission, SuperstudentPermission
from .serializers import RegistrationSerializer, RoleAssignmentSerializer, UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = get_user_model().objects.create_user(
                request.data['email'],
                request.data['first_name'],
                request.data['last_name'],
                request.data['password']
            )
            data['email'] = request.data['email']
            data['name'] = request.data['first_name'] + " " + request.data['last_name']
            data['token'] = Token.objects.get(user=user).key
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST'])
@permission_classes([AdminPermission | SuperstudentPermission])
def role_assignment_view(request):
    if request.method == "POST":

        serializer = RoleAssignmentSerializer(data=request.data)
        if serializer.is_valid():

            if request.user.role == 'SU' and request.data['role'] == 'AD':
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "Superstudent can't make someone Admin", "field": "role"
                            }
                        ]
                    }, code='not allowed')

            user = get_user_model().objects.get(email=request.data['email'])

            if not user:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "user does not exist", "field": "email"
                            }
                        ]
                    }, code='invalid')

            user.role = request.data['role']
            user.save()
            data = {'message': f'{user.email} is nu een {user.get_role_display()}'}
        else:
            data = serializer.errors
        return Response(data)
