"""Synthetic job routing for the commit context benchmark."""

def uses_background_queue(attempt: int) -> bool:
    return attempt > 1
