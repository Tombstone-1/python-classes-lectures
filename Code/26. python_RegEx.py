"""
Python Regular Expression
A regex is a sequence of characters that forms a search pattern
regex can be used to check if a string contains the specified search pattern.

"""

# RegEx Module
# Python has a built-in package called re, which can be used to work with regular expressions.
import re 

txt = "The rain in Spain"
x = re.search("^The. *Spain$", txt)

if x:
    print("yes ! we have match")
else:
    print("no match")

"""
All RegEx Functions
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
"""

"""
RegEx Meta Characters
[]	A set of characters	            "[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	    "he..o"	
^	Starts with	                "^hello"	
$	Ends with	                "planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	    "he.+o"	
?	Zero or one occurrences	    "he.?o"	
{}	Exactly the specified number of occurrences	    "he.{2}o"	
|	Either or	                "falls|stays"
"""

"""
RegEx Flags
re.ASCII	    re.A	Returns only ASCII matches	
re.DEBUG		        Returns debug information	
re.DOTALL	    re.S	Makes the . character match all characters (including newline character)	
re.IGNORECASE	re.I	Case-insensitive matching	
re.MULTILINE	re.M	Returns only matches at the beginning of each line	
re.NOFLAG		        Specifies that no flag is set for this pattern	
re.UNICODE	    re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
re.VERBOSE	    re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable
"""

# use findall() method - > return list of all matching words
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# the list contain the matches in the order they are found.
# if no match, empty list return

# Return an empty list if no match was found
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# using search() function.
# search the string for a match and return a match object, if matched.
# if more that more match return only first occurance.
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# if not match found, None returned.

# Example : search that return no match
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# using split() function
# return a list where the string has been split at each match.
# Example : split at each white-space character
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# can control the number of occurrences by specifying the maxsplit parameter
# example :  split the string only at the first occurrence.
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)          # <<-- this 1 is maxsplit parameter.
print(x)

# using sub() function
# replace the matches with the text of your choice.
# Example : replace every white-space with number 9:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)      # <-- second parameter replaces stuff.
print(x)

# You can control the number of replacements by specifying the count parameter.
# Example : replace with the first 2 occurrences
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)       # < second one for replacementm, fourth one is for occurrences count.
print(x)

# using match object
# A Match Object is an object containing information about the search and the result.
# example : to return match object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match

"""
# Example : Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# example : Print the string passed into the function:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# example : Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())





