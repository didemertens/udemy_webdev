from oop_farm_animalcl import *

class Cow(Animals):
  def __init__(self):
    super().__init__(15,15,10)
    self._type = "Cow"

  def grow(self,water,food):
    if water >= self._water_need and food >= self._food_need:
      if self._status == "Baby" and food > self._food_need:
        self._weight += self._growth_rate * 1.5
      if self._status == "Young" and food > self._food_need:
        self._weight += self._growth_rate * 1.25
      else:
        self._weight += self._growth_rate
    self._days_growing += 1
    self._update_status()


if __name__ == "__main__":
  main()
