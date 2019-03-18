try:
  f = open("simple.txt",'r')
  f.write("test write to simple text")
except IOError:
  print("Couldn't find file or read data.")
else:
  print("Success!")
  f.close()
finally:
  print("Always be printed")

