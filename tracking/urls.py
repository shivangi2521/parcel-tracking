from django.urls import path
from .views import TrackingNumberView

# Define URL patterns for the tracking number API
urlpatterns = [
    # Route for generating the next tracking number.
    # Maps the URL 'next-tracking-number' to the TrackingNumberView.
    # The 'name' allows referencing this URL in templates or reverse calls.
    path(
        "next-tracking-number",
        TrackingNumberView.as_view(),
        name="next-tracking-number",
    ),
]
