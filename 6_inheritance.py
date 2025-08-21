# # parent, base, super class
# class Animal:

#     def speak(self):
#         print('animal speaks')

# # child, derived, sub class
# class Dog(Animal):
#     pass


# dog1 = Dog()
# dog1.speak()

# # single inheritance

# class Vehicle:

#     def start(self):
#         print('vehical started')

# class Car(Vehicle):

#     def nitro_boost(self):
#         print('nitro boost actiavted')

# car1 = Car()
# car1.start()
# car1.nitro_boost()

# # multilevel inheritance

# class Device():

#     def power_on(self):
#         print('device power on...')

# class Computer(Device):

#     def boot(self):
#         print('booting up...')

# class Laptop(Computer):

#     def portable(self):
#         print('I am portable...')

# laptop = Laptop()
# computer = Computer()

# computer.power_on()
# computer.boot()

# # laptop.power_on()
# # laptop.boot()
# # laptop.portable()

# # hierarchical inheritance

# class Payment:

#     def pay(self):
#         print('paying...')

# class CreditCardPayment(Payment):

#     def pay(self):
#         print('credit card payment')

# class UPIPayment(Payment):

#     def pay(self):
#         print('upi payment mode')

# credicardobj = CreditCardPayment()
# upiobj = UPIPayment()
# # credicardobj.pay()
# upiobj.pay()

# # multiple inheritance

# class Wallet:

#     def add_money(self):
#         print('wallet...')

# class Reward:

#     def redeem_points(self):
#         print('reward...')

# class DigitalWallet(Wallet, Reward):

#     def pay(self):
#         print('payyy...')

# dw = DigitalWallet()
# dw.pay()
# dw.add_money()
# dw.redeem_points()

# class A:
#     def show(self):
#         pass

# class B(A):
#     def show(self):
#         pass

# class C(B):
#     def show(self):
#         pass

# c = C()
# c.show()
# print(C.mro())

# class A:
#     def greet(self):
#         print('hello from A')

# class B(A):
#     def greet(self):
#         print('hello from B')
#         super().greet()

# b = B()
# b.greet()
# print(B.mro())


# diamond problem
class A:

    def show(self):
        print('A')

class B(A):
    
    def show(self):
        print('B')

class C(A):
    
    def show(self):
        print('C')

class D(C, B):
    pass

d = D()
d.show()

print(D.mro())