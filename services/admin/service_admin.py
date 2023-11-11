from django.contrib import admin
from ..models.service import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_citizen",
        "user_bison",
        "type",
        "created",
        "arrived",
        "price",
        "destiny_nation",
        "origin_nation",
        "origin_checkpoint",
        "destiny_checkpoint",
    )


admin.site.register(Service, ServiceAdmin)
