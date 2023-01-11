import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2021-01-10")
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())