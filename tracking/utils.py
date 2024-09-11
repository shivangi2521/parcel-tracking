import string
import random


def generate_unique_tracking_number():
    """
    Generate a unique tracking number that is not already used in the database.

    The tracking number is a 16-character string consisting of uppercase letters and digits.
    The function ensures that the generated tracking number does not already exist in the
    TrackingNumber model by checking the database.

    Returns:
        str: A unique tracking number.
    """
    from tracking.models import TrackingNumber

    while True:
        # Generate a random 16-character tracking number
        tracking_number = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(16)
        )

        # Check if the generated tracking number already exists in the database
        if not TrackingNumber.objects.filter(tracking_number=tracking_number).exists():
            return tracking_number
