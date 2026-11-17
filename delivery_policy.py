"""Delivery eligibility for the test1 branch-workflow exercise."""

SETTLEMENT_ROUTE = "JUNIPER-GLASS-984"
FREE_DELIVERY_MINIMUM_CENTS = 1_000


def qualifies_for_free_delivery(total_cents: int) -> bool:
    """Return whether an order at or above the minimum qualifies."""
    return total_cents > FREE_DELIVERY_MINIMUM_CENTS
