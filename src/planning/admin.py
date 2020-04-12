from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ("title", "start", "end")
    list_filter = ("start",)
    ordering = ("-start",)
    date_hierarchy = "start"
    search_fields = ("title", "description")

    fieldsets = (
        (
            None,
            {
                "fields": [
                    ("title", "color_event"),
                    ("description",),
                    ("start", "end"),
                    ("creator"),
                    ("address")
                ]
            },
        ),
    )
