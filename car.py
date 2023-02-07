from battery import Battery
from engine import Engine


class Car(Engine,Battery):
    def __init__(self, battery,engine):
        self.battery = battery
        self.engine = engine

    def battery_needs_service(self):
        return self.battery.needs_service()  
    
    def engine_needs_service(self):
        return self.engine.needs_service()

    def needs_service(self):
        return self.battery_needs_service() or self.engine_needs_service()
