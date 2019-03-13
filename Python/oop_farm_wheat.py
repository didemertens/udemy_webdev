from oop_farm_gencrop import *

class Wheat(Crop):
  """A wheat crop"""
  def __init__(self):
    super().__init__(1,3,4)
    self._type = "Wheat"

  def grow(self,light,water):
    if light >= self._light_need and water >= self._water_need:
      if self._status == "Seedling":
        self._growth += self._growth_rate * 1.5
      elif self._status == "Young":
        self._growth += self._growth_rate * 1.25
      elif self._status == "Old":
        self._growth += self._growth_rate / 2
      else:
        self._growth += self._growth_rate
    self._days_growing += 1
    self._update_status()


def main():
  # Create new wheat crop
  wheat_crop = Wheat()


if __name__ == "__main__":
  main()

