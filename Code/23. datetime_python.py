# python Date
"""
a date time is not a data type of its own, but we can import a module 
named datetime to work with dat objects
"""
# example
import datetime

x = datetime.datetime.now()
print(x)
# date output <-- 2025-08-25 21:12:48.298308
# the date contains year, month, day, hour, minute, second and microsecond.

# example :2

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# create Date objects
# to create a date, use datetime() class constructor of the datetime module.
# datetime() require 3 parameters : year, month, day

x = datetime.datetime(2020, 5 17)
print(x)
# datetime() class also takes parameters for time and timezone(hour, minute, second, microsecond, tzone)
# but they are optional and has default value of 0.

# use : strftime() method
# takes one parameter, format to specify the format
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))     # <-- this inside bracket () is format specifier.


