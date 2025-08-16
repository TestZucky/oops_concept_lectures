# # Public 

# class Demo:

#     def __init__(self):
#         self.name = 'zucky'

# obj = Demo()
# print(obj.name)

# # Protected

# class Demo:

#     def __init__(self):
#         self._name = 'zucky'

# obj = Demo()
# print(obj._name)

# private

class Demo:

    def __init__(self):
        self.__name = 'zucky'

obj = Demo()
print(obj.__dict__)