# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# syntax
# lambda arguments : expression

# Why use Lambda function ?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n

# example 1
x = lambda a : a + 10
print(x(5))     # <-- return 15

# example 2
x = lambda a, b : a * b
print(x(5, 6))  # <-- return 30

# example 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))   # <-- return 13
