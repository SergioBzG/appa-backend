from django.db import models

from services.models.service import Service


class Package(models.Model):
    service = models.OneToOneField(
        Service,
        primary_key=True,
        verbose_name="ID",
        on_delete=models.CASCADE,
    )
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(weight__gte=1) & models.Q(weight__lte=500),
                name="valid_weight",
            ),
            models.CheckConstraint(
                check=models.Q(length__gte=1) & models.Q(length__lte=1000),
                name="valid_length",
            ),
            models.CheckConstraint(
                check=models.Q(width__gte=1) & models.Q(width__lte=1000),
                name="valid_width",
            ),
            models.CheckConstraint(
                check=models.Q(height__gte=1) & models.Q(height__lte=1000),
                name="valid_height",
            )
        ]


