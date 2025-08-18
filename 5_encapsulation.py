# class Student:
    
#     def __init__(self, name, age, grade):
#         self.name = name # public
#         self._age = age # protected
#         self.__grade = grade # private

# s = Student('Bob', 45, 'A')
# print(s.name)
# print(s._age)
# print(s._Student__grade)

# # (traditional way)
# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     # setter
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
    
#     # getter
#     def get_balance(self):
#         return self.__balance
    

# b1 = BankAccount(100)
# print(b1.get_balance())
# b1.deposit(200)
# print(b1.get_balance())


# (pythonic way)
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def deposit(self):
        pass

    # setter
    @deposit.setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    # getter
    @property
    def get_balance(self):
        return self.__balance
    

b1 = BankAccount(100)
print(b1.get_balance)
b1.deposit = 200
print(b1.get_balance)
