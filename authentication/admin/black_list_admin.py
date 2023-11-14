from django.contrib import admin
from ..models.black_list import BlackListedToken


class BlackListedTokenAdmin(admin.ModelAdmin):
    list_display = (
        "token",
        "user",
        "created_at",
    )


admin.site.register(BlackListedToken, BlackListedTokenAdmin)
