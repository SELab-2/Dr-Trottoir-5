from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.middleware import csrf
from rest_framework import serializers, generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import AdminPermission, SuperstudentPermission, ReadOnly
from .serializers import RegistrationSerializer, RoleAssignmentSerializer, UserPublicSerializer, UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['GET'])
@permission_classes([ReadOnly])
def user_view(request):
    response = Response()
    if request.user.is_authenticated:
        response.data = UserSerializer(request.user).data
        return response
    else:
        response.data = "{'error': 'no user'}"
        return response


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    data = request.data
    response = Response()
    username = data.get('email', None)
    password = data.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            data = get_tokens_for_user(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=data["access"],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
                value=data["refresh"],
                expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            response.data = UserSerializer(user).data
            return response
        else:
            return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == "POST":
        response = Response()
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = get_user_model().objects.create_user(
                request.data['email'],
                request.data['first_name'],
                request.data['last_name'],
                request.data['password']
            )
            refresh = RefreshToken.for_user(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=str(refresh.access_token),
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
                value=str(refresh),
                expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.data = UserSerializer(user).data
        else:
            response.data = serializer.errors
        return response


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
