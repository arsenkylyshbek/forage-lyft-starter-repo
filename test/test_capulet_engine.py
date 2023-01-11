import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def should_be_serviced(self):
        # last_service_date = datetime.today().year

        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())