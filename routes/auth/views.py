from django.contrib.auth import authenticate
from django.utils import timezone
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import User
from .serializers import LoginSerializers, AuthSerializer, RegisterSerializer, PasswordResetSerializer
from .exceptions import UserAuthException
from .tasks import send_email_verification_mail, send_password_reset_email


@api_view(['POST'])
def login_view(request):
    login_serializer = LoginSerializers(data=request.data)
    if login_serializer.is_valid():
        user = authenticate(**login_serializer.data)
        if not user:
            raise UserAuthException

        if 'REMOTE_ADDR' in request.META:
            user.last_login_ip = request.META['REMOTE_ADDR']

        user.last_login = timezone.now()
        user.save()
        serializer = AuthSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        raise UserAuthException


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    # Check for valid data
    if serializer.is_valid():
        try:
            # checking for existing user
            existing_user = User.objects.get(email=request.data['email'])

            # If users exists with the corresponding email then send an exception
            return Response(data={'detail': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            # Saving the user to database
            user = serializer.save()

            # Check for email validations
            if settings.USER_EMAIL_VERIFICATION:

                # sending email to user
                send_email_verification_mail(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # Send execption if we get some invalid details
        return Response(data={'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def verify_email(request, verification_token):
    try:
        user = User.objects.get(email_verification_token=verification_token)
        user.email_verification_token = None
        user.is_email_verified = True
        user.save()

        return Response(data={'detail': 'Email verified successfully'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(data={'detail': 'Invalid Link'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def password_reset(request):
    email = request.data['email']
    try:
        user = User.objects.get(email=email)
        send_password_reset_email(user)

        return Response(data={'detail': 'Password Reset Email has been set'})

    except User.DoesNotExist:
        return Response(data={'detail': 'No account exists with this email id'})


@api_view(['POST'])
def password_reset_confirm(request, reset_token):
    try:
        user = User.objects.get(password_reset_token=reset_token)
        if not timezone.now() <= user.password_reset_expiry:
            return Response(data={'detail': 'Password reset link has been expired'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.data['password']
            user.set_password(password)

            user.password_reset_token = None
            user.password_reset_expiry = None

            user.save()

            return Response(data={'detail': 'Password reset successfull'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'detail': 'Please enter valid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response(data={'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
