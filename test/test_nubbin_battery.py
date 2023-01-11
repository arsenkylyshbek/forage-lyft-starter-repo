import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def should_be_serviced(self):
        today = datetime.today().year
        last_service_date = today - 3
        engine = NubbinBattery(today, last_service_date)
        self.assertTrue(engine.needs_service())

    def should_not_be_serviced(self):
        today = datetime.today().year
        last_service_date = today
        engine = NubbinBattery(today, last_service_date)
        self.assertFalse(engine.needs_service())
