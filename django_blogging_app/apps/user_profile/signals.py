from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from django.contrib.auth import get_user_model

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our App!'
        message = f'Hi {instance.username},\n\nWelcome to our app. Thank you for registering!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)
