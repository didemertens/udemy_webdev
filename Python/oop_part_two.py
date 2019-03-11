class Dog():

  # class object attribute
  species = "mammal"

  def __init__(self,breed,name):
    self.breed = breed
    self.name = name



mydog = Dog('labrador','Sam')
# print(mydog.breed)
# print(mydog.species)


class Circle():

  pi = 3.14

  def __init__(self, radius=1):
    self.radius = radius

  def area(self):
    return self.radius * self.radius * Circle.pi

  def set_radius(self,new_r):
    self.radius = new_r


myc = Circle(radius=3)
# myc.radius = 10
myc.set_radius(10)

print(myc.area())
