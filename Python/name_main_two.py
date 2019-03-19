import name_main

print("TOP LEVEL name_main_two.py")

name_main.func()

if __name__ == '__main__':
  print("name_main_two.py directly")
else:
  print("name_main_two.py imported")
