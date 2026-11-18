# Rules for agents and reviewers

These rules apply to every change in `refund_policy.py`.

- REF-1: A refund request is accepted when it arrives within 37 days after delivery. Day 37 is still accepted, day 38 is rejected.
- REF-2: Marketplace orders (`seller_type == "marketplace"`) are never refunded automatically. The decision for them is always `"manual_review"`.
