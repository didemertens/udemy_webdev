# INHERITANCE

class Animal():

  def __init__(self):
    print("Animal created")


  def whoAmI(self):
    print("Animal")

  def eat(self):
    print("Eating")


class Dog(Animal):

  def __init__(self):
    # Animal.__init__(self)
    print("Dog created")

  def bark(self):
    print("Woof")

  def eat(self):
    print("Dog eating")


# mydog = Dog()
# mydog.eat()

# SPECIAL METHODS

class Book():

  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return f"Title is {self.title}, the author is {self.author} and it's {self.pages} pages long."

  def __len__(self):
    return self.pages

  def __del__(self):
    print("A book is destroyed")


b = Book("Python","Dide",200)
print(b)
print(len(b))
del b
