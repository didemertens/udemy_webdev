class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# sam = Dog("Sam",9)
# bobby = Dog("Bobby",2)
# # nora = Dog("Nora",4)

# def get_biggest_number(*args):
#   return max(args)

# oldest = get_biggest_number(sam.age,bobby.age,nora.age)
# print(f"The oldest dog is {oldest} years old.")

class Pets:

    animals = []

    def __init__(self, animals):
        self.animals = animals

    def amount_pets(self):
      return f"I have {len(self.animals)} pets."


my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

# my_pets = Pets(my_dogs)
# print(my_pets.amount_pets())

# for dog in my_dogs:
#   print(f"{dog.name} is {dog.age} years old.")

# print(f"And they are all {dog.species}s of course.")
for dog in my_dogs:
  dog.eat()

dogs_are_hungry = False
for dog in my_dogs:
  if dog.is_hungry:
    dogs_are_hungry = True

if dogs_are_hungry == True:
  print("My dogs are hungry")
else:
  print("My dogs are not hungry.")




