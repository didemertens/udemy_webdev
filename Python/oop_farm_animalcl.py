class Animals:

  def __init__(self, growth_rate,water_need,food_need):
    self._growth_rate = growth_rate
    self._water_need = water_need
    self._food_need = food_need
    self._weight = 5
    self._days_growing = 0
    self._status = "Baby"
    self._type = "Generic"
    self._name = "Animal"

  def needs(self):
    return {'water need': self._water_need, 'food_need':self._food_need}

  def report(self):
    return {'name': self._name, 'type':self._type, 'status':self._status, 'weight':self._weight, 'days growing':self._days_growing}

  def _update_status(self):
    if self._weight > 60:
      self._status = "Old"
    elif self._weight > 30:
      self._status = "Mature"
    elif self._weight > 15:
      self._status = "Young"
    elif self._weight == 5:
      self._status = "Baby"

  def grow(self,water,food):
    if water >= self._water_need and food >= self._food_need:
      self._weight += self._growth_rate
    self._days_growing += 1
    self._update_status()

# def main():
#   myanimal = Animals(10,10,10)
#   print(myanimal.report())
#   myanimal.grow(20,20)
#   print(myanimal.report())

if __name__ == "__main__":
  main()

