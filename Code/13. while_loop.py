# Python has 2 loops 
# syntax
i = 1
while i < 6:
  print(i)
  i += 1
# remember to increment i or else the loop wil continue forever.

# break statement stop loop from inside.
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# example : continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# will skip when continue condition is true.

# example : else statement when condition is no longer is true.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

