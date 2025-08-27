# condition command
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
# example : if
a = 33
b = 200
if b > a:
  print("b is greater than a")
# pay proper attention to indentation or else python wil give error.

# example : elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# example : else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# example : short hand if
if a > b: print("a is greater than b")

# example : short hand if else
a = 2
b = 330
print("A") if a > b else print("B")
# this technique is known as ternary operators or conditional expression.

# example : multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# example : and , or, not keyword
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")
if not a > b:
  print("a is NOT greater than b")

# Example : Nested if 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Example : pass statement.
a = 33
b = 200

if b > a:
  pass      # <--- pass keyword or statement get used wherever you need to leave some indented statement without context.

 