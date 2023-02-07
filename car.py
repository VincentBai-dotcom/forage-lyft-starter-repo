from battery import Battery
from engine import Engine
from tire import Tire


class Car(Engine,Battery):
    def __init__(self, battery,engine,tire):
        self.battery = battery
        self.engine = engine
        self.tire = tire

    def battery_needs_service(self):
        return self.battery.needs_service()  
    
    def engine_needs_service(self):
        return self.engine.needs_service()

    def tire_needs_service(self):
        return self.tire.needs_service()

    def needs_service(self):
        return self.battery_needs_service() or self.engine_needs_service() or self.tire_needs_service()
