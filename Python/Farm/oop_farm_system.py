from oop_farm_wheat import *
from oop_farm_potato import *

def display_menu():
  print()
  print("Which crop would you like to create?")
  print()
  print("1. Potato")
  print("2. Wheat")
  print()
  print("Please select an option from the above menu.")

def select_option():
  valid_option = False
  while not valid_option:
    try:
      choice = int(input("Option selected: "))
      if choice in (1,2):
        valid_option = True
      else:
        print("Choice not valid.")
    except ValueError:
      print("Choice not valid.")
  return choice

def create_crop():
  display_menu()
  choice = select_option()
  if choice == 1:
    new_crop = Potato()
  if choice == 2:
    new_crop = Wheat()
  return new_crop

def main():
  new_crop = create_crop()
  manage_crop(new_crop)

if __name__ == "__main__":
  main()
