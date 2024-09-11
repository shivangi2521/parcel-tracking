from django.urls import path
from .views import TrackingNumberView

urlpatterns = [path("next-tracking-number", TrackingNumberView.as_view())]
