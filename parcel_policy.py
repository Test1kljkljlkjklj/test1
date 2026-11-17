"""Parcel size policy for a test1 draft review exercise."""


def is_standard_parcel(width_cm: int) -> bool:
    """Standard parcels must have a positive width no greater than 60 cm."""
    return 0 <= width_cm <= 60
