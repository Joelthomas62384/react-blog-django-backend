from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserProfileManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import uuid
from django.conf import settings



class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True)
    bio = models.TextField(blank=True, null=True, max_length=500)
    is_email_verified = models.BooleanField(default=False,null=True, blank=True)
    is_phone_verified = models.BooleanField(default=False,null=True, blank=True)
    otp  = models.CharField(max_length=200, blank=True, null=True)
    email_verfication_token = models.CharField(max_length=200, blank=True, null=True)
    forgot_password_token = models.CharField(max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserProfileManager()

    def __str__(self):
        return self.username


@receiver(post_save, sender=UserProfile)
def send_email_token(sender,instance,created, **kwargs):
    try:
        subject = "Your Email needs to be verified"
        message = f"Hi the Otp to verify your email is {instance.otp}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject,message,email_from,recipient_list)



    except Exception as e:
        print(e)
