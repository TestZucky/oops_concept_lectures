
# paranterized constructor
# class Person:

#     def __init__(self, name, age):
#         print('constructor called')
#         self.name = name
#         self.age = age

# p = Person("John", 34)
# print(p.name, p.age)

# # default constructor
# class Empty:
#     pass

# obj = Empty()
# print(obj)

class Demo:

    def __new__(cls, *args, **kwargs):
        print('inside new')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        print('inside init')
        self.value = value

demo = Demo(10)
    