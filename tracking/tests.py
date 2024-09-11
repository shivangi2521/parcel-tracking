from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from uuid import uuid4
from .models import TrackingNumber


class TrackingNumberViewTests(TestCase):
    """
    Test suite for the TrackingNumber API view.
    """

    def setUp(self):
        """
        Set up test data and configuration before each test.
        """
        self.client = APIClient()
        self.url = reverse(
            "next-tracking-number"
        )  # Adjust if you use a different URL name

        # Define valid parameters for creating a TrackingNumber
        self.valid_params = {
            "origin_country_id": "MY",
            "destination_country_id": "ID",
            "weight": "1.234",
            "created_at": "2024-09-11T00:00:00+00:00",
            "customer_id": str(uuid4()),  # Generate a unique UUID
            "customer_name": "RedBox Logistics",
            "customer_slug": "redbox-logistics",
            "tracking_number": "MA0V3WWCLMUF3QJZ",  # Note: This is an example; tracking numbers should be unique
        }

    def test_create_tracking_number_success(self):
        """
        Test successful creation of a TrackingNumber.
        """
        response = self.client.get(self.url, self.valid_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("tracking_number", response.data)
        self.assertIn("created_at", response.data)
        # Ensure that the tracking number follows the expected format
        self.assertRegex(response.data["tracking_number"], r"^[A-Z0-9]{1,16}$")

    def test_create_tracking_number_invalid_uuid(self):
        """
        Test creation of a TrackingNumber with an invalid UUID.
        """
        invalid_params = self.valid_params.copy()
        invalid_params["customer_id"] = "invalid-uuid"  # Set an invalid UUID
        response = self.client.get(self.url, invalid_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["error"], "Invalid customer_id, must be a valid UUID."
        )

    def test_tracking_number_uniqueness(self):
        """
        Test that the tracking number is unique.
        """
        # Create the first tracking number
        self.client.get(self.url, self.valid_params)
        # Attempt to create another tracking number with the same parameters
        response = self.client.get(self.url, self.valid_params)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Ensure the new tracking number is different from the previous one
        self.assertNotEqual(
            response.data["tracking_number"], self.valid_params["tracking_number"]
        )

    def test_create_tracking_number_invalid_weight(self):
        """
        Test creation of a TrackingNumber with invalid weight.
        """
        invalid_params = self.valid_params.copy()
        invalid_params["weight"] = "invalid-weight"  # Set an invalid weight
        response = self.client.get(self.url, invalid_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
