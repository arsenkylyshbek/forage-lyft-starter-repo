from datetime import datetime
from battery.spindler_battery import SpindlerBattery
import unittest



class TestSpindlerBattery(unittest.TestCase):
    def should_be_serviced(self):
        today = datetime.today().year
        last_service_date = today - 5
        engine = SpindlerBattery(today, last_service_date)
        self.assertTrue(engine.needs_service())

    def should_not_be_serviced(self):
        today = datetime.today().year
        last_service_date = today
        engine = SpindlerBattery(today, last_service_date)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
