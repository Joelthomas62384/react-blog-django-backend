from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None, address='', phone_number='', **extra_fields):
        if not email or not username:
            raise ValueError('Users must have an email address and a username')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            address=address,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, address='', phone_number='', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            email=email,
            username=username,
            password=password,
            address=address,
            phone_number=phone_number,
            **extra_fields
        )
