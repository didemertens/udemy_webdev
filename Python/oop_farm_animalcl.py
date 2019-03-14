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
    return {'water need:' self._water_need, 'food_need':self._food_need}

  def report(self):
    return {'name': self._name, 'type':self._type, 'status':self._status, 'weight':self.weight, 'days growing':self._days_growing}

  def _update_status(self):
    elif self._weight > 60:
      self._status = "Old"
    elif self._weight > 30:
      self._status = "Mature"
    elif self._weight > 15:
      self._status = "Young"
    elif self._weight == 0:
      self._weight = "Baby"

  def grow(self,water,food):
    if water >= self._water_need and food >= self._food_need:
      self._weight += self._growth_rate
    self._days_growing += 1
    self._update_status()

class Cows(Animals):
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

