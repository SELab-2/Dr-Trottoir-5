from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import serializers, generics
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import get_user_model
from .permissions import AdminPermission, SuperstudentPermission, ReadOnly, StudentPermission
from .serializers import RegistrationSerializer, RoleAssignmentSerializer, UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]


class UserRetrieveDestroyView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(email=request.user)
            return Response(UserSerializer(user).data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced user not in db", "field": "token"
                        }
                    ]
                }, code='invalid')

    def partial_update(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(email=request.user)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response({"succes": ["Updated user"]})
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced user not in db", "field": "token"
                        }
                    ]
                }, code='invalid')


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
                request.data['phone_nr'],
                request.data['password']
            )
            data['email'] = request.data['email']
            data['name'] = request.data['first_name'] + " " + request.data['last_name']
            refresh = RefreshToken.for_user(user)
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    """
        Send an email with an otp when forgot password is used.
    """
    email = request.data['email']
    user = get_user_model().objects.get(email=email)
    if get_user_model().objects.filter(email=email).exists():
        send_mail(
            subject='Nieuw wachtwoord voor Dr Trottoir.',
            message=f'{user.otp}',  # TODO  email text schrijven
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            auth_user=settings.DEFAULT_FROM_EMAIL,
            auth_password=settings.EMAIL_HOST_PASSWORD
        )
        return Response({'message': 'Email is verstuurd'})
    else:
        return Response({'message': 'Dit email adres bestaat niet.'})


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    """
        Reset the password with the otp that is received via email.
    """
    data = request.data
    try:
        user = get_user_model().objects.get(email=data['email'])
    except Exception:
        raise serializers.ValidationError(
            {"errors": [
                {
                    "message": "There is no user with this email", "field": "email"
                }
            ]
            }, code='invalid')
    else:
        if data['otp'] == user.otp:
            if data['new_password'] != '':
                user.set_password(data['new_password'])
                user.save()  # Will automatically create new otp
                return Response({'message': 'New password is created'})
            else:
                raise serializers.ValidationError(
                    {
                        "errors": [{"message": "Password can't be empty", "field": "new_password"}]
                    }, code='invalid')
        else:
            raise serializers.ValidationError(
                {
                    "errors": [{"message": "OTP didn't match", "field": "otp"}]
                }, code='invalid')


@api_view(['POST', 'GET'])
@permission_classes([AdminPermission | SuperstudentPermission | ReadOnly])
def role_assignment_view(request):
    if request.method == "GET":  # return role of user
        return Response({'role': request.user.role})

    if request.method == "POST":  # change the role of a user
        serializer = RoleAssignmentSerializer(data=request.data)
        if serializer.is_valid():

            if request.user.role == 'SU' and request.data['role'] == 'AD':
                raise serializers.ValidationError(
                    {
                        "errors": [{"message": "Superstudent can't make someone Admin", "field": "role"}]
                    }, code='not allowed')

            user = get_user_model().objects.get(email=request.data['email'])

            if not user:
                raise serializers.ValidationError(
                    {
                        "errors": [{"message": "user does not exist", "field": "email"}]
                    }, code='invalid')

            user.role = request.data['role']
            user.save()
            data = {'message': f'{user.email} is nu een {user.get_role_display()}'}
        else:
            data = serializer.errors
        return Response(data)
