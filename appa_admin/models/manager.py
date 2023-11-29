from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from authentication.models import Role


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """

        if not email:
            raise ValueError(_("The email must be set"))

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Set role to AVATAR by default
        role: Role = Role.objects.filter(name="AVATAR").first()
        if role:
            extra_fields.setdefault("role", role)
        else:
            role = Role.objects.create(name="AVATAR", description="Manager of the system")
            extra_fields.setdefault("role", role)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)

    def create(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
