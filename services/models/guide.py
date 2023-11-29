from django.db import models

from services.models.service import Service


class Guide(models.Model):
    guide_number = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="ID",
        editable=False,
    )
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
    )
    current_nation = models.CharField(max_length=50)
    current_checkpoint = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(current_nation__in=[
                    "Nación del Aire", "Nación del Fuego", "Nación de la Tierra", "Nación del Agua"
                ]),
                name="valid_current_nation",
            ),
            models.CheckConstraint(
                check=models.Q(current_checkpoint__in=[
                    "Tribu agua del norte",
                    "Tribu agua del sur",
                    "Tribu aire del norte",
                    "Tribu aire del este",
                    "Tribu aire del oeste",
                    "Tribu aire del sur",
                    "Ba Sing Se",
                    "Abadía",
                    "Gaipan",
                    "Si Wong",
                    "Capital nación del fuego",
                    "Shu Jing"
                ]),
                name="valid_current_checkpoint",
            )
        ]

    def __str__(self):
        return f"Guide number: {self.guide_number}"