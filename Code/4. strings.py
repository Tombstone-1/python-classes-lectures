# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello". both allowed.

# Example
print("Hello")
print('Hello')

# Ouotes inside Outes (print word surrounded by quotes)
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline strings will just look like multiline comments just that you will be adding it to a variable.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# or single qoutes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# notes here line breaks are as in the code, means print will output same as you written in code.

# Strings as arrays.
# note : in python char is not a datatype. a single character in a variable will still be consider a string.
# square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])


# Looping through a strings.
for x in "banana":
  print(x)

# string lengths. len() function.
a = "Hello, World!"
print(len(a))

# check Strings.
txt = "The best things in life are free!"
print("free" in txt)
# also can be used in if statement.
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# check if not.
txt = "The best things in life are free!"
print("expensive" not in txt)
# same in if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Slicing Strings
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])       # remember it won't print 5 character, only from 0 to 4.

# slicing from the start.
b = "Hello, World!"
print(b[:5])

# slicing from the end.
b = "Hello, World!"
print(b[2:])

# negative slicing. numbering start from right side and from -1.
b = "Hello, World!"
print(b[-5:-2])   # print from only (o) to (l). second position in slicing bracket i.e 'd' in world (position -2 itself) will not be included.


# Modify strings.
# upper case.
a = "Hello, World!"
print(a.upper())

# Lower case
a = "Hello, World!"
print(a.lower())

# remove whitespace
a = " Hello, World! "
print(a.strip()) # output "Hello, World!"

# replace string
a = "Hello, World!"
print(a.replace("H", "J")) # output "jello, world!"

# spilt string (The split() method returns a list where the text between the specified separator becomes the list items.)
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# String Concatenation.
# to combine and join to string use + operator.

# example merge a with into c
a = "Hello"
b = "World"
c = a + b
print(c)

# concatenate with spaces
a = "Hello"
b = "World"
c = a + " " + b
print(c)


### Strings Format.
# previously if remembered string and no. can't be combine together
# so we can use f-strings for that. from python 3.6 onwards.

# To use F-string or format string ( specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.)
# example
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers.
# A placeholder can contain variables, operations, functions, and modifiers to format the value.
# Example
price = 59
txt = f"The price is {price} dollars"  # here price inside {} is complete known as placeholders.
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
# example : display price with 2 decimals only.
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# placeholder can also do math operations.
# Ex :  do multiplication inside placeholder.
txt = f"The price is {20 * 59} dollars"
print(txt)


# Escape Characters in Python.
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# example : output string with double quotes.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # double quotes inside double quotes is illegal , we can use this to put double quotes.

""" All Escape Characters 
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""

# Strings Methods. remember string methods return new values, they do not change original string.
"""
capitalize()	  Converts the first character to upper case
casefold()	    Converts string into lower case
center()	      Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	      Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	  Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	      Formats specified values in a string
format_map()	  Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	      Returns True if all characters in the string are alphanumeric
isalpha()	      Returns True if all characters in the string are in the alphabet
isascii()	      Returns True if all characters in the string are ascii characters
isdecimal()   	Returns True if all characters in the string are decimals
isdigit()	      Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	      Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()  	Returns True if all characters in the string are printable
isspace()     	Returns True if all characters in the string are whitespaces
istitle()	      Returns True if the string follows the rules of a title
isupper()     	Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()      	Returns a left trim version of the string
maketrans()   	Returns a translation table to be used in translations
partition()   	Returns a tuple where the string is parted into three parts
replace()	      Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	      Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	  Returns a tuple where the string is parted into three parts
rsplit()	      Splits the string at the specified separator, and returns a list
rstrip()	      Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	  Splits the string at line breaks and returns a list
startswith()	  Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning

"""