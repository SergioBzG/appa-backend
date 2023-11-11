from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..models.user import User
# Register your models here.


class CustomUserAdmin(UserAdmin):
    """
    Class to customize the user administration panel
    """

    model = User
    list_display = (
        "id",
        "name",
        "document",
        "email",
        "phone",
        "vehicle",
        "available",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "available",
        "email",
    )
    fieldsets = (
        ("Information", {"fields": ("name",
                                    "document",
                                    "email",
                                    "phone",
                                    "vehicle",
                                    "available",
                                    )}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "document",
                    "email",
                    "phone",
                    "vehicle",
                    "available",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email", "name", "document", "phone", "vehicle")
    ordering = ("id",)


admin.site.register(User, CustomUserAdmin)
