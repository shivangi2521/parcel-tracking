from django.db import models
from uuid import uuid4
from .utils import generate_unique_tracking_number


class TrackingNumber(models.Model):
    """
    Model to represent a tracking number with associated details.
    """

    tracking_number = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_id = models.UUIDField(default=uuid4)  # UUID for the customer
    origin_country_id = models.CharField(
        max_length=2, blank=True
    )  # Country code for the origin (optional)
    destination_country_id = models.CharField(
        max_length=2, blank=True
    )  # Country code for the destination (optional)
    weight = models.DecimalField(
        max_digits=5, decimal_places=3, blank=True, null=True
    )  # Weight of the item in the tracking number (optional)
    customer_name = models.CharField(
        max_length=255, blank=True
    )  # Name of the customer (optional)
    customer_slug = models.SlugField(
        blank=True
    )  # Slug for the customer's name (optional)

    def save(self, *args, **kwargs):
        """
        Override the save method to set a unique tracking number if not provided.
        """
        if not self.tracking_number:
            self.tracking_number = generate_unique_tracking_number()
        super().save(*args, **kwargs)
