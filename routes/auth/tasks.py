import uuid
from smtplib import SMTPException
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
        print('EMAIL ERROR')
