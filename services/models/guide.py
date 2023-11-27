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
                    "NACION DEL AIRE", "NACION DEL FUEGO", "NACION DE LA TIERRA", "NACION DEL AGUA"
                ]),
                name="valid_current_nation",
            ),
            models.CheckConstraint(
                check=models.Q(current_checkpoint__in=[
                    "TRIBU AGUA DEL NORTE",
                    "TRIBU AGUA DEL SUR",
                    "TRIBU AIRE DEL NORTE",
                    "TRIBU AIRE DEL ESTE",
                    "TRIBU AIRE DEL OESTE",
                    "TRIBU AIRE DEL SUR",
                    "BA SING SE",
                    "ABADIA",
                    "GAIPAN",
                    "SI WONG",
                    "CAPITAL NACION DEL FUEGO",
                    "SHU JING"
                ]),
                name="valid_current_checkpoint",
            )
        ]

    def __str__(self):
        return f"Guide number: {self.guide_number}"