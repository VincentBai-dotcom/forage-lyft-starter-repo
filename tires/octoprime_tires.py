from tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, sensory_data):
        self.sensory_data = sensory_data

    def needs_service(self):
        sum = 0
        for worness in self.sensory_data:
            sum += worness
        if sum >=3:
            return True
        return False
