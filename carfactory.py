import engine, battery
from car import Car


class CarFactory:
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = engine.capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        bat = battery.spindler_battery.SpindlerBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = engine.willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        bat = battery.spindler_battery.SpindlerBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = engine.willoughby_engine.CapuletEngine(current_mileage, last_service_mileage)
        bat = battery.nubbin_battery.NubbinBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = engine.capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        bat = battery.nubbin_battery.NubbinBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        eng = engine.sternman_engine.SternmanEngine(warning_light_is_on)
        bat = battery.spindler_battery.SpindlerBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car
