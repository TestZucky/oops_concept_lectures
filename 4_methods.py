class Car:

    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    # instance method
    def show_details(self):
        print(f"Brand - {self.brand}, color - {self.color}, wheels - {self.wheels}")

    # class method
    @classmethod
    def show_wheel_count(cls):
        print(f'Wheel count - {cls.wheels}')

    # static method
    @staticmethod
    def say_my_brand(brand):
        print(f'brand is {brand}')


# car1 = Car('BMW', 'blue')
# car1.show_details()
# car1.show_wheel_count()

Car.say_my_brand("Toyota")