"""Refund decisions for delivered orders."""

REFUND_WINDOW_DAYS = 30


def refund_decision(order: dict, days_since_delivery: int) -> str:
    """Return "approved" or "rejected" for a refund request."""
    if days_since_delivery < 0:
        return "rejected"
    if days_since_delivery <= REFUND_WINDOW_DAYS:
        return "approved"
    return "rejected"
