import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def should_be_serviced(self):
        # last_service_date = datetime.today().year

        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())