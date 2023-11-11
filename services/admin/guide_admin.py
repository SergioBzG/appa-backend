from django.contrib import admin
from ..models.guide import Guide


class GuideAdmin(admin.ModelAdmin):
    list_display = (
        "guide_number",
        "service",
        "current_nation",
        "current_checkpoint",
    )


admin.site.register(Guide, GuideAdmin)
