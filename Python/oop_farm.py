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


def auto_grow(crop,days):
  for i in range(days):
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
  crop.grow(light,water)

def main():
  new_crop = Crop(1,4,3)
  # print(new_crop.needs()['light need'])
  # print(new_crop.report())
  # new_crop.grow(5,5)
  manual_grow(new_crop)
  print(new_crop.report())




if __name__ == "__main__":
  main()
