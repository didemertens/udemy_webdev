my_stuff = {'key1':'clothes', 'key2':'books'}

for key in my_stuff:
  print(my_stuff[key])

mypairs = [(1,2),(3,4),(5,6)]

# tuple unpacking
for (tup1,tup2) in mypairs:
  print(tup1)
  print(tup2)

# Computer just saves 1 number at a time when generating with range
mylist = list(range(0,10,2))
print(mylist)

for item in range(10):
  print(item)

x = [1,2,3,4]

out = []

out = [num**2 for num in x]

print(out)
