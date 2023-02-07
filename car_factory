from car import Car
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class CarFactory():

    def __init__(self):
        pass

    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage):
        battery = NubbinBattery(last_service_date,current_date)
        engine = CapuletEngine(current_mileage,last_service_mileage)
        car = Car(battery,engine)
        return car

    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage):
        battery = NubbinBattery(last_service_date,current_date)
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        car = Car(battery,engine)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_on):
        battery = SpindlerBattery(last_service_date,current_date)
        engine = SternmanEngine(warning_light_on)
        car = Car(battery,engine)
        return car

    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage):
        battery = SpindlerBattery(last_service_date,current_date)
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        car = Car(battery,engine)
        return car

    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage):
        battery = SpindlerBattery(last_service_date,current_date)
        engine = CapuletEngine(current_mileage,last_service_mileage)
        car = Car(battery,engine)
        return car
