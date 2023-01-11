import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2019-05-10")
        engine = SpindlerBattery(today, last_service_date)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        today = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2022-05-15")
        engine = SpindlerBattery(today, last_service_date)
        self.assertFalse(engine.needs_service())
