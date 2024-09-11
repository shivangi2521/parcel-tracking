from django.contrib import admin
from .models import TrackingNumber

# Register your models here.


class TrackingNumberModelAdmin(admin.ModelAdmin):
    list_display = [
        "tracking_number",
        "customer_id",
        "origin_country_id",
        "destination_country_id",
        "weight",
        "customer_name",
        "customer_slug",
    ]
    readonly_fields = ["tracking_number"]


admin.site.register(TrackingNumber, TrackingNumberModelAdmin)
