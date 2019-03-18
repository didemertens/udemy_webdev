# s = "Global"

# def func():
#   # global s
#   # s = 50
#   # print(s)
#   mylocal = 10
#   print(locals())
#   print(globals()['s'])



# def hello(name='Dide'):
#   return "Hello "+name

# mynewgreet = hello
# Assiging functions to variables


# def hello(name='Dide'):
#   print('hello function has been run')

#   def greet():
#     return "This string is inside greet"

#   def welcome():
#     return "This string is inside welcome"

#   if name == "Dide":
#     return greet
#   else:
#     return welcome
#     #return entire function, not the string

# x = hello()

# print(x())


# def hello():
#   return "Hi Dide"

# def other(func):
#   print("hello")
#   print(func())

# other(hello)

def new_dec(func):

  def wrap_func():
    print("code executing func")
    func()
    print("func() has been called")

  return wrap_func

@new_dec
def func_needs_dec():
  print("This func needs a decorator")

# func_needs_dec = new_dec(func_needs_dec)


func_needs_dec()


