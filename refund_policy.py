"""Refund decisions for delivered orders."""

# Окно возврата в днях после доставки (REF-1).
REFUND_WINDOW_DAYS = 42


def refund_decision(order: dict, days_since_delivery: int) -> str:
    """Return "approved", "rejected" or "manual_review" for a refund request."""
    if days_since_delivery < 0:
        return "rejected"
    if order.get("product_type") == "gift_card":
        return "rejected"
    if order.get("seller_type") == "marketplace":
        return "manual_review"
    if days_since_delivery <= REFUND_WINDOW_DAYS:
        return "approved"
    return "rejected"
