from celery import shared_task
from django.contrib.auth import get_user_model 
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
import sys


def send_email(user) : 
    
    html = render_to_string("send_activation_email.html",context={"code":user.otp})
    message = EmailMultiAlternatives(
        subject="activation code",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    message.attach_alternative(html,"text/html")
    message.send()

@shared_task
def send_otp_code(email) : 
    user = get_user_model().objects.get(email=email)
    user.save()
    sys.stdout.write(f"CODE : {user.otp}")
    # send_email(user=user)