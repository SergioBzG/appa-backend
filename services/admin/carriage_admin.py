from django.contrib import admin
from ..models.carriage import Carriage


class CarriageAdmin(admin.ModelAdmin):
    list_display = (
        "service",
        "pick_up",
        "description",
    )


admin.site.register(Carriage, CarriageAdmin)
