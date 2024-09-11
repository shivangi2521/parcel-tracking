from django.db import models
from uuid import uuid4
from .utils import generate_unique_tracking_number


class TrackingNumber(models.Model):
    tracking_number = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_id = models.UUIDField(default=uuid4)  # Use customer's actual UUID
    origin_country_id = models.CharField(max_length=2, blank=True)  # Optional
    destination_country_id = models.CharField(max_length=2, blank=True)  # Optional
    weight = models.DecimalField(
        max_digits=5, decimal_places=3, blank=True, null=True
    )  # Optional
    customer_name = models.CharField(max_length=255, blank=True)  # Optional
    customer_slug = models.SlugField(blank=True)  # Optional

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = generate_unique_tracking_number()
        super().save(*args, **kwargs)
