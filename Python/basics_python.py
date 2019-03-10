# Lists
mylist = ['a','b','c']

anotherlist = ['d','e','f']

mylist.extend(anotherlist)
# print(mylist)


mylist.pop(2)
# print(mylist)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]
# print(first_col)

# Dict
my_stuff = {'key1':'clothes', 'key2':'books','key3':{'123':[1,2,"grabme"]}}

# print(my_stuff['key3']['123'][2].upper())

# Tuples
t = (1,2,3)

# Sets (unique, unordered)
x = set()
x.add(1)
x.add(2)
x.add(2)
x.add(4)
# print(x)

converted = set([1,1,1,1,1,2,2,2,2,3])
print(converted)
