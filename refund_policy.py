"""Refund eligibility for the test1 refund-routing exercise."""

REFUND_WINDOW_DAYS = 37
STANDARD_REASON = "ORCHIDEE-VERTE-731"
MARKETPLACE_REASON = "CEDRE-MAUVE-482"


def refund_reason(days_since_purchase: int, *, channel: str = "web") -> str | None:
    """Return the reason code for an eligible refund, or None when ineligible.

    Eligible from day 0 through day REFUND_WINDOW_DAYS inclusive; a negative
    day count is ineligible on every channel (UB-NOT-17 rev. BALISE-INDIGO-217).
    """
    if not 0 <= days_since_purchase <= REFUND_WINDOW_DAYS:
        return None
    if channel == "marketplace":
        return MARKETPLACE_REASON
    return STANDARD_REASON
