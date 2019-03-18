import random

class Crop:

  """A generic food crop"""

  def __init__(self,growth_rate,light_need,water_need):
    self._growth_rate = growth_rate
    self._light_need = light_need
    self._water_need = water_need
    self._growth = 0
    self._days_growing = 0
    self._status = "Seed"
    self._type = "Generic"

  def needs(self):
    return {'light need':self._light_need, 'water need':self._water_need}

  def report(self):
    return {'type':self._type, 'status':self._status, 'growth':self._growth, 'days growing':self._days_growing}

  def _update_status(self):
    if self._growth > 15:
      self._status = 'Old'
    elif self._growth > 10:
      self._status = 'Mature'
    elif self._growth > 5:
      self._status = 'Young'
    elif self._growth > 0:
      self._status = 'Seedling'
    else:
      self._status = 'Seed'

  def grow(self,light,water):
    if light >= self._light_need and water >= self._water_need:
      self._growth += self._growth_rate
    self._days_growing += 1
    self._update_status()


def auto_grow(crop):
  for i in range(30):
    light = random.randint(1,10)
    water = random.randint(1,10)
    crop.grow(light,water)

def manual_grow(crop):
  valid = False
  while not valid:
    try:
      light = int(input('Enter a value for light (1-10): '))
      if 1 <= light <= 10:
        valid = True
      else:
        print("Value not valid - please try again.")
    except ValueError:
      print("Value not valid - please try again.")

  valid = False
  while not valid:
    try:
      water = int(input('Enter a value for water (1-10): '))
      if 1 <= water <= 10:
        valid = True
      else:
        print("Value not valid - please try again.")
    except ValueError:
      print("Value not valid - please try again.")
  # Grow the crop
  crop.grow(light,water)

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

def manage_crop(crop):
  print("This is the crop management program.")
  print()
  noexit = True
  while noexit:
    display_menu()
    option = get_choice_menu()
    if option == 1:
      manual_grow(crop)
      print()
    elif option == 2:
      auto_grow(crop)
      print()
    elif option == 3:
      print(crop.report())
      print()
    elif option == 0:
      noexit = False
  print("See you later!")

def main():
  new_crop = Crop(1,4,3)
  # print(new_crop.needs()['light need'])
  # print(new_crop.report())
  # new_crop.grow(5,5)
  manage_crop(new_crop)


if __name__ == "__main__":
  main()
