# x = 5
# print(type(x))

class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def get_brand_color(self):
        print(f'Brand: {self.brand}, color: {self.color}')


car1 = Car('Toyota', 'Red') # object
car2 =Car('BMW', 'Blue')
car1.get_brand_color()
car2.get_brand_color()
