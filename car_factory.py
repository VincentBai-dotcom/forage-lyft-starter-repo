from car import Car
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory():

    def __init__(self):
        pass

    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage,sensory_data):
        battery = SpindlerBattery(last_service_date,current_date)
        engine = CapuletEngine(current_mileage,last_service_mileage)
        tire = CarriganTires(sensory_data)
        car = Car(battery,engine,tire)
        return car

    def create_glissade(self,current_date,last_service_date,current_mileage,last_service_mileage,sensory_data):
        battery = SpindlerBattery(last_service_date,current_date)
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        tire = CarriganTires(sensory_data)
        car = Car(battery,engine,tire)
        return car

    def create_palindrome(self,current_date, last_service_date, warning_light_on,sensory_data):
        battery = NubbinBattery(last_service_date,current_date)
        engine = SternmanEngine(warning_light_on)
        tire = CarriganTires(sensory_data)
        car = Car(battery,engine,tire)
        return car

    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage,sensory_data):
        battery = NubbinBattery(last_service_date,current_date)
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        tire = OctoprimeTires(sensory_data)
        car = Car(battery,engine,tire)
        return car

    def create_thovex(self,current_date,last_service_date,current_mileage,last_service_mileage,sensory_data):
        battery = NubbinBattery(last_service_date,current_date)
        engine = CapuletEngine(current_mileage,last_service_mileage)
        tire = OctoprimeTires(sensory_data)
        car = Car(battery,engine,tire)
        return car
