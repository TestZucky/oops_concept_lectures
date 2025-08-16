class Dog:
    species = 'canis family' # class attributes

    def __init__(self, name, color):
        self.name = name # instance attributes
        self.color = color # instance attributes

    def bark(self):
        print(f'Bark...')

    def say_my_name(self):
        print(f'My name is {self.name}, color is {self.color}')

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Species: {self.species}"
        


dog1 = Dog(name='Puppy', color='brown')
dog2 = Dog(name='John', color='black')

print(dog1)
print(dog2)


# dog1.say_my_name()
# dog2.say_my_name()

# print(dog1.name)
# print(dog2.name)

# print(dog1.species)
# print(dog2.species)

