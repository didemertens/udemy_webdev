from oop_farm_animalcl import *


class Sheep(Animals):
  def __init__(self):
    super().__init__(10,5,5)
    self._type = "Sheep"

  def grow(self,water,food):
    if water >= self._water_need and food >= self._food_need:
      if self._status == "Baby" and food > self._food_need:
        self._weight += self._growth_rate * 2.25
      if self._status == "Young" and food > self._food_need:
        self._weight += self._growth_rate * 1.5
      else:
        self._weight += self._growth_rate
    self._days_growing += 1
    self._update_status()

def main():
  my_sheep = Sheep()
  print(my_sheep.report())

if __name__ == "__main__":
  main()
