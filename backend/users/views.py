from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.core.mail import send_mail
from django.middleware import csrf
from rest_framework import serializers, generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from exceptions.exceptionHandler import ExceptionHandler
from .permissions import AdminPermission, SuperstudentPermission, ReadOnly, StudentPermission, \
    SyndicusPermission
from .serializers import RoleAssignmentSerializer, \
    UserPublicSerializer, UserSerializer


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


@api_view(['GET', 'PATCH'])
@permission_classes([SyndicusPermission | StudentPermission | SuperstudentPermission | AdminPermission])
def user_view(request):
    response = Response()
    if request.method == 'GET':
        if request.user.is_authenticated:
            response.data = UserSerializer(request.user).data
        else:
            response.data = "{'error': 'no user'}"
    elif request.method == 'PATCH':
        if request.user.is_authenticated:
            data = request.data
            serializer = UserSerializer(request.user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response.data = serializer.data
            else:
                response.data = serializer.errors
        else:
            response.data = "{'error': 'no user'}"
    return response


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    data = request.data
    response = Response()
    email = data.get('email', None)
    password = data.get('password', None)

    handler = ExceptionHandler()
    handler.check_not_blank_required(email, "email")
    handler.check_not_blank_required(password, "password")
    handler.check_email(email, User)
    handler.check()

    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            data = get_tokens_for_user(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=data["access"],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
                value=data["refresh"],
                expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            response.data = UserSerializer(user).data
            return response
        else:
            return Response({"No active": "This account is not active!!"},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"errors": [{"message": "Verkeerd wachtwoord.", "field": "password"}]},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    logout(request=request)
    response = Response({"message": "You have been logged out succefully"})
    response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
    response.delete_cookie(settings.SIMPLE_JWT['REFRESH_COOKIE'])
    return response


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == "POST":
        response = Response()
        data = request.data

        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("email"), "email")
        handler.check_not_blank_required(data.get("first_name"), "firstname")
        handler.check_not_blank_required(data.get("last_name"), "lastname")
        handler.check_not_blank_required(data.get("password"), "password")
        handler.check_not_blank_required(data.get("password2"), "password2")
        handler.check_integer_required(data.get("phone_nr"), "phone_nr")
        handler.check_equal(data.get("password"), data.get("password2"), "password2")
        handler.check()

        if get_user_model().objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({
                "errors": [{
                    "message": "Dit email adres is al in gebruik.",
                    "field": "email"
                }]})

        user = get_user_model().objects.create_user(
            request.data['email'],
            request.data['first_name'],
            request.data['last_name'],
            request.data['phone_nr'],
            request.data['password']
        )
        refresh = RefreshToken.for_user(user)
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=str(refresh.access_token),
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.set_cookie(
            key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
            value=str(refresh),
            expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.data = UserSerializer(user).data

        return response


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    """
        Send an email with an otp when forgot password is used.
    """

    data = request.data
    email = data["email"]

    handler = ExceptionHandler()
    handler.check_not_blank_required(email, "email")
    handler.check_email(email, User)
    handler.check()

    user = get_user_model().objects.get(email=email)
    send_mail(
        subject='Nieuw wachtwoord voor Dr Trottoir.',
        message=f'{user.otp}',  # TODO  email text schrijven
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        auth_user=settings.DEFAULT_FROM_EMAIL,
        auth_password=settings.EMAIL_HOST_PASSWORD
    )
    return Response({'message': 'Email is verstuurd'})


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    """
        Reset the password with the otp that is received via email.
    """
    data = request.data
    email = data.get("email")
    otp = data.get("otp")
    password = data.get("password")
    password2 = data.get("password2")

    handler = ExceptionHandler()
    handler.check_not_blank_required(email, "email")
    handler.check_not_blank_required(otp, "otp")
    handler.check_not_blank_required(password, "password")
    handler.check_not_blank_required(password2, "password2")
    handler.check_email(email, User)
    handler.check()

    user = get_user_model().objects.get(email=data['email'])

    handler.check_equal(password, password2, "password2")
    handler.check_equal(otp, user.otp, "otp")
    handler.check()

    user.set_password(password)
    user.save()  # Will automatically create new otp
    return Response({'message': 'New password is created'})


@api_view(['PATCH', 'GET'])
@permission_classes([AdminPermission | SuperstudentPermission | ReadOnly])
def role_assignment_view(request):
    if request.method == "GET":  # return role of user
        return Response({'role': request.user.role})

    if request.method == "PATCH":  # change the role of a user
        serializer = RoleAssignmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            if request.user.role == 'SU' and request.data['role'] == 'AD':
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "Superstudent can't make someone Admin",
                                "field": "role"
                            }
                        ]
                    }, code='not allowed')

            try:
                user = get_user_model().objects.get(
                    email=request.data['email'])
            except get_user_model().DoesNotExist:
                user = None

            if not user:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {"message": "user does not exist",
                             "field": "email"}
                        ]
                    }, code='invalid')

            user.role = request.data['role']
            user.save()
            data = {
                'message': f'{user.email} is nu een {user.get_role_display()}'}
        else:
            data = serializer.errors
        return Response(data)


class UserByIdRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]

    def patch(self, request, *args, **kwargs):
        data = request.data

        id = kwargs['pk']
        handler = ExceptionHandler()
        handler.check_primary_key(id, 'id', User)
        handler.check_not_blank(data.get("email"), "email")
        handler.check_not_blank(data.get("first_name"), "first_name")
        handler.check_not_blank(data.get("last_name"), "last_name")
        handler.check_not_blank(data.get("password"), "password")
        handler.check_integer(data.get("phone_nr"), "phone_nr")
        handler.check()

        user = get_user_model().objects.get(id=id)

        if user.email != data.get("email") and get_user_model().objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({
                "errors": [{
                    "message": "Dit email adres is al in gebruik.",
                    "field": "email"
                }]
            })
        return super().patch(request, *args, **kwargs)
