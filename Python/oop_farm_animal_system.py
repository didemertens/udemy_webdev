import random
from oop_farm_cow import *
from oop_farm_sheep import *

def manual_grow(animal):
  choice_valid = False
  while not choice_valid:
    try:
      food = int(input("Enter a value for food (1-30): "))
      if 1 <= food <= 30:
        choice_valid = True
      else:
        print("Please enter a valid choice.")
    except ValueError:
      print("Please enter a valid choice.")

    choice_valid = False
    while not choice_valid:
      try:
        water = int(input("Enter a value for water (1-30): "))
        if 1 <= water <= 30:
          choice_valid = True
        else:
          print("Please enter a valid choice.")
      except ValueError:
        print("Please enter a valid choice.")
  animal.grow(water, food)

def automatic_grow(animal):
  for i in range(30):
    water = random.randint(10,30)
    food = random.randint(10,30)
  animal.grow(water,food)

def main():
  my_cow = Cows()
  print(my_cow.report())
  manual_grow(my_cow)
  print(my_cow.report())


if __name__ == "__main__":
  main()
