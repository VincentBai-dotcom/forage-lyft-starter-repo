from tire import Tire

class CarriganTires(Tire):
    def __init__(self, sensory_data):
        self.sensory_data = sensory_data

    def needs_service(self):
        for worness in self.sensory_data:
            if worness >=0.9:
                return True
        return False
