from django.db import models


class Role(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="ID",
        editable=False,
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=80)

    def __str__(self):
        return self.name
