from django.db import models

from services.models.service import Service


class Carriage(models.Model):
    service = models.OneToOneField(
        Service,
        primary_key=True,
        verbose_name="ID",
        on_delete=models.CASCADE,
    )
    pick_up = models.DateTimeField()
    description = models.CharField(max_length=200)
