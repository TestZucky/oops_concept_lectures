from abc import ABC, abstractmethod

# contract
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

    def horn(self):
        print('hornnnnn...')

class Car(Vehicle):

    def start_engine(self):
        print('car engine started')

    def stop_engine(self):
        print('car engine stopped')

    def build_roof(self):
        print('car roof have been created')

class Bike(Vehicle):

    def start_engine(self):
        print('bike engine started')

    def stop_engine(self):
        print('bike engine stopped')

car = Car()
car.start_engine()
car.stop_engine
car.build_roof()