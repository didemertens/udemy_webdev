import random
from oop_farm_cow import *
from oop_farm_sheep import *

def display_animal():
  print()
  print("Which animal would you like to create?")
  print()
  print("1. Cow")
  print("2. Sheep")
  print()
  print("Please select an option from the above menu.")

def select_option():
  valid_option = False
  while not valid_option:
    try:
      choice = int(input("Option selected: "))
      print()
      if choice in (1,2):
        valid_option = True
      else:
        print("Choice not valid.")
    except ValueError:
      print("Choice not valid.")
  return choice

def create_animal():
  display_animal()
  choice = select_option()
  if choice == 1:
    new_animal = Cow()
  if choice == 2:
    new_animal = Sheep()
  return new_animal

def display_menu():
  print("1. Grow manually over 1 day")
  print("2. Grow automatically over 30 days")
  print("3. Report status")
  print("0. Exit test program")
  print()
  print("Please select an option from the above menu.")
  print()

def get_choice_menu():
  option_valid = False
  while not option_valid:
    try:
      choice = int(input("Option selected: "))
      if 0 <= choice <= 4:
        option_valid = True
      else:
        print("Please enter a valid option.")
    except ValueError:
      print("Please enter a valid option.")
  return choice

def manage_animal(animal):
  print("This is the animal management program.")
  print()
  noexit = True
  while noexit:
    display_menu()
    option = get_choice_menu()
    if option == 1:
      manual_grow(animal)
      print()
    elif option == 2:
      auto_grow(animal)
      print()
    elif option == 3:
      print(animal.report())
      print()
    elif option == 0:
      noexit = False
  print("See you later!")

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

def auto_grow(animal):
  for i in range(30):
    water = random.randint(10,30)
    food = random.randint(10,30)
  animal.grow(water,food)

def main():
  new_animal = create_animal()
  manage_animal(new_animal)



if __name__ == "__main__":
  main()
