import string
import random


def generate_unique_tracking_number():
    from tracking.models import TrackingNumber

    while True:
        tracking_number = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(16)
        )
        if not TrackingNumber.objects.filter(tracking_number=tracking_number).exists():
            return tracking_number
