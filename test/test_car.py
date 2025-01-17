import sys
sys.path.append("/Users/baihaocheng/Documents/forage/lyft/forage-lyft-starter-repo/")
import unittest
from datetime import datetime

from car_factory import CarFactory

class TestCalliope(unittest.TestCase):
    factory = CarFactory()

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_calliope(today,last_service_date,current_mileage,last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_calliope(today,last_service_date,current_mileage,last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_calliope(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_calliope(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    factory = CarFactory()
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]
        
        car = self.factory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    factory = CarFactory()
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        sensory_data = [0,0,0,0]

        car = self.factory.create_palindrome(today,last_service_date, warning_light_is_on,sensory_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        sensory_data = [0,0,0,0]

        car = self.factory.create_palindrome(today,last_service_date, warning_light_is_on,sensory_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        sensory_data = [0,0,0,0]

        car = self.factory.create_palindrome(today,last_service_date, warning_light_is_on,sensory_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        sensory_data = [0,0,0,0]

        car = self.factory.create_palindrome(today,last_service_date, warning_light_is_on,sensory_data)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    factory = CarFactory()
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    factory = CarFactory()
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensory_data = [0,0,0,0]

        car = self.factory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())


class TestTires(unittest.TestCase):
    factory = CarFactory()
    def test_carrigan_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0.89,0,0,0]

        car = self.factory.create_calliope(today,last_service_date,current_mileage,last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())

    def test_carrigan_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensory_data = [0.9,0.98,0,0]

        car = self.factory.create_calliope(today,last_service_date,current_mileage,last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())

    def test_octoprime_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensory_data = [1,1,0.9,0]

        car = self.factory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertFalse(car.needs_service())

    def test_octoprime_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensory_data = [1,1,1,0]

        car = self.factory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,sensory_data)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
