from rest_framework import serializers
from .models import TrackingNumber


class TrackingNumberSerializer(serializers.ModelSerializer):
    """
    Serializer for the TrackingNumber model.

    This serializer handles the conversion of TrackingNumber objects to and from JSON format
    for use in API responses and requests.
    """

    class Meta:
        model = TrackingNumber  # Specify the model to be serialized
        fields = (
            "tracking_number",  # The unique tracking number for the shipment
            "created_at",  # The date and time when the tracking number was created
            "customer_id",  # UUID identifying the customer
            "origin_country_id",  # The 2-character country code for the origin (optional)
            "destination_country_id",  # The 2-character country code for the destination (optional)
            "weight",  # The weight of the item being tracked (optional)
            "customer_name",  # The name of the customer (optional)
            "customer_slug",  # A slugified version of the customer's name (optional)
        )
