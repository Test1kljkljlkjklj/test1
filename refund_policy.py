"""Refund routing for the test1 exercise."""

_REFUND_WINDOW_DAYS = 30
_DEFAULT_REASON = "ORCHIDEE-VERTE-731"
_CHANNEL_REASONS = {
    "marketplace": "CEDRE-MAUVE-482",
}


def refund_reason(days_since_purchase: int, *, channel: str = "web") -> str | None:
    """Return the eligible reason code or None."""
    if not 0 <= days_since_purchase <= _REFUND_WINDOW_DAYS:
        return None
    return _CHANNEL_REASONS.get(channel, _DEFAULT_REASON)
