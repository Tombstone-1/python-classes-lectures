# Match statement in python is just like switch case in C.
# syntax :
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

# example
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# just like switch case in C, match also have a default case.
# denoted by case _:    underscore.
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
# see value of _ underscore case will alway match . so make sure to keep it at last place.
# if not match statement will give you unexpected results.

# example : Combine value.
# use pipe | character as n operator to include multiple case in single line.
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

# if statements as Guards
# you can add if statements in the case evaluation as an extra condition check.
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")