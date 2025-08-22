# # instance method

# class Car:

#     wheels = 4

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def show_details(self):
#         print(f'Car brand - {self.brand}, color - {self.color}, wheels - {self.wheels}')

# car1 = Car('BMW', 'Blue')
# car1.show_details()



# # class method

# class Car:

#     wheels = 4

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def show_details(self):
#         print(f'Car brand - {self.brand}, color - {self.color}, wheels - {self.wheels}')

#     @classmethod
#     def show_wheels(cls):
#         print(f'wheels - {cls.wheels}, brand - {cls.brand}')

# car1 = Car('BMW', 'Blue')
# car1.show_details()
# car1.show_wheels()




# static method

class Car:

    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def show_details(self):
        print(f'Car brand - {self.brand}, color - {self.color}, wheels - {self.wheels}')

    @classmethod
    def show_wheels(cls):
        print(f'wheels - {cls.wheels}')

    @staticmethod
    def drive():
        print('Drive.....')

car1 = Car('BMW', 'Blue')
car1.show_details()
car1.show_wheels()
Car.drive()