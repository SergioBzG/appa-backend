from django.contrib import admin
from ..models.role import Role


# Register your models here.
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
    )

admin.site.register(Role, RoleAdmin)
