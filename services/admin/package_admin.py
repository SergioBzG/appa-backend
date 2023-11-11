from django.contrib import admin
from ..models.package import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "service",
        "length",
        "width",
        "height",
        "weight",
    )


admin.site.register(Package, PackageAdmin)
