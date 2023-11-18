from django.db import models

from appa_admin.models.user import User


class Service(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="ID",
        editable=False,
    )
    user_citizen = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="citizen_orders",
    )
    user_bison = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="bison_orders",
        null=True,
    )
    type = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    arrived = models.DateTimeField(null=True, blank=True)
    price = models.IntegerField()
    destiny_nation = models.CharField(max_length=50)
    origin_nation = models.CharField(max_length=50)
    origin_checkpoint = models.CharField(max_length=50)
    destiny_checkpoint = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(destiny_nation__in=[
                    "Nación del Aire", "Nación del Fuego", "Nación de la Tierra", "Nación del Agua"
                ]),
                name="valid_destiny_nation",
            ),
            models.CheckConstraint(
                check=models.Q(origin_nation__in=[
                    "Nación del Aire", "Nación del Fuego", "Nación de la Tierra", "Nación del Agua"
                ]),
                name="valid_origin_nation",
            ),
            models.CheckConstraint(
                check=models.Q(origin_checkpoint__in=[
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
                name="valid_origin_checkpoint",
            ),
            models.CheckConstraint(
                check=models.Q(destiny_checkpoint__in=[
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
                name="valid_destiny_checkpoint",
            ),
            models.CheckConstraint(
                check=models.Q(type__in=["CARRIAGE", "PACKAGE"]),
                name="valid_type",
            )
        ]

    def __str__(self):
        return f"{self.id} - {self.type}"
