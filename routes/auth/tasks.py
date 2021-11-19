import uuid
import logging
from smtplib import SMTPException
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings


def send_email_verification_mail(user):
    # Generate activation token
    activation_token = uuid.uuid4().hex

    try:
        # Send email
        send_mail('Email Verification', f'Activatation link {settings.EMAIL_VERIFICATION_LINK}/{activation_token}',
                  'support@snippetclass.io', [user.email], fail_silently=False)

        # Save the activation token to user model
        user.email_verification_token = activation_token
        user.save()
    except SMTPException:
        logging.error(f'Email Can not be sent - {user.email}')


def send_password_reset_email(user):
    user.password_reset_token = uuid.uuid4().hex
    user.password_reset_expiry = timezone.now() + timezone.timedelta(minutes=5)

    try:
        # Send email
        send_mail('Password Reset Token', f'Reset Token - {user.password_reset_token}',
                  'support@snippetclass.io', [user.email], fail_silently=False)

        # Save the reset token to user model
        user.save()
    except SMTPException:
        logging.error(f'Email Can not be sent - {user.email}')
