# # method overriding (RTP) (Dynamic)

# class Payment:

#     def pay(self, amount):
#         print(f'Paying {amount} with generic method')

# class UPI(Payment):

#     def pay(self, amount):
#         print(f'Paying {amount} via UPI')


# class Card(Payment):

#     def pay(self, amount):
#         print(f'Paying {amount} via card')

# p1 = UPI()
# p2 = Card()

# for payment in (p1, p2):
#     payment.pay(100)

# # method overloading (Compile time polymorphism) (Static polymorphism)

# class MathUtil:

#     # def add(self, a, b):
#     #     return a+b
    
#     # def add(self, a, b, c=0):
#     #     return a +b +c

#     def add(self, *args):
#         return sum(args)
    
# m = MathUtil()
# print(m.add(10,20, 30))


# operator overloading

# print(10+20)
# print('10'+'20')

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __str__(self):
#         return f"{self.x}, {self.y}"

# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# print(f'Number1 --> {v1}')
# print(f'Number2 --> {v2}')
# print(v1+v2)

# v1.__add__(v2)


class Shape:
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
    
class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

shape1 = Circle(5)
shape2 = Rectangle(10,20)

print(shape1.area())
print(shape2.area())


















