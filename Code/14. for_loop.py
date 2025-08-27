# syntax
# range_statement like a string, list, tuple and such.
for element in range_statement:
    print(element)

# example : from list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# example : loop through a string 
for x in "banana":
  print(x)

# example : break statement 
# break with stop the loop when condition are met.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# example : continue statement
# continue will skip the point where condition are met.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# example : range() method.
# by default range start from 0, and increment by 1
# range(0,10.1) --> range(start, end, steps/ direction) direction (+ve no measn forward, -ve means backward)
for x in range(6):  
    print(x)    
# 6 does not means its a value, its end range (not included) because range start from 0.

# example : else in for loop
# here else block means it will run when loop is finished
# remember else block won't run if there's break statement in loop.
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# using break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

### nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# example : using pass statement
# used when for some reason your for loop is empty.
for x in [0, 1, 2]:
  pass


