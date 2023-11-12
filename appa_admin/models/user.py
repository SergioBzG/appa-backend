from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

from authentication.models.role import Role


class User(AbstractUser):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="ID",
        editable=False,
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True, related_name="users"
    )
    document = models.CharField(max_length=50, unique=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=25, unique=True, null=True)
    vehicle = models.CharField(max_length=10, unique=True, null=True)
    available = models.BooleanField(default=True)

    # Remove username field and use email as unique identifier
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["role", "name"]

    # Use custom user manager
    objects = UserManager()

    def __str__(self):
        return self.name
