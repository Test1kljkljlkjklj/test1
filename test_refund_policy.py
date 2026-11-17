import unittest

from refund_policy import refund_reason


class RefundReasonTest(unittest.TestCase):
    def test_day_37_is_eligible(self):
        self.assertEqual(refund_reason(37), "ORCHIDEE-VERTE-731")

    def test_day_38_is_ineligible(self):
        self.assertIsNone(refund_reason(38))

    def test_marketplace_within_window_uses_marketplace_code(self):
        self.assertEqual(refund_reason(37, channel="marketplace"), "CEDRE-MAUVE-482")

    def test_marketplace_past_deadline_is_ineligible(self):
        self.assertIsNone(refund_reason(38, channel="marketplace"))

    def test_other_channel_uses_standard_code(self):
        self.assertEqual(refund_reason(10, channel="Marketplace"), "ORCHIDEE-VERTE-731")


if __name__ == "__main__":
    unittest.main()
