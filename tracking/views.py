from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TrackingNumber
from .serializers import TrackingNumberSerializer
from .utils import generate_unique_tracking_number
from uuid import UUID
from django.core.exceptions import ValidationError


class TrackingNumberView(APIView):
    """
    API view for creating a new TrackingNumber object.
    """

    def get(self, request):
        """
        Handle GET requests to create a new TrackingNumber.
        """
        try:
            # Validate and parse the customer_id as a UUID
            customer_id = request.GET.get("customer_id")
            if customer_id:
                try:
                    customer_id = UUID(customer_id)
                except ValueError:
                    return Response(
                        {"error": "Invalid customer_id, must be a valid UUID."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            # Create a new TrackingNumber object
            tracking_number = TrackingNumber.objects.create(
                tracking_number=generate_unique_tracking_number(),
                customer_id=customer_id,
                origin_country_id=request.GET.get("origin_country_id", ""),  # Optional
                destination_country_id=request.GET.get(
                    "destination_country_id", ""
                ),  # Optional
                weight=request.GET.get("weight", None),  # Optional
                customer_name=request.GET.get("customer_name", ""),  # Optional
                customer_slug=request.GET.get("customer_slug", ""),  # Optional
            )

            # Serialize the TrackingNumber object
            serializer = TrackingNumberSerializer(tracking_number)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred: " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
