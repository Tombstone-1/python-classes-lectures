# Python allows User Input

# example
print("Enter your name:")
name = input()
print(f"Hello {name}")

# python stops executing when it comes to input() function and continues when the user has given some input.
# using prompt
name = input("Enter your name:")
print(f"Hello {name}")

# Multiple inputs
# add many inputs and python will wait for every input()
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# Input number
# by default input from user is treated as string, 
# if want other datatype you can just type cast it.
# Example : change it to float
x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")

# or
x = float(input("enter float"))

# Concept validate Input
"""
It is a good practice to validate any input from the user. 
In the example above, an error will occur if the user inputs something other than a number.

"""
# Example : keep asking until receive a number
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")



