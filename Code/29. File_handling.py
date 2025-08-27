# python File handling #
"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

"""

# file handling functions
# using open()
"""
"r" : for read -> raise error if file does not exist
"a" : for append - > open a file to inserting. create the file if does not exist
"w" : for write - > create file if does not exist.
"x" : for create -> create specified file, return error if file of same name and type already exist

# you can specify if the file should be handled as binary or text mode.

"t" : Text file - Default value text mode
"b" : binary file -  binary mode for like images.

"""

# syntax
f = open("demofile.txt", "rt")  # (filename.txt, operation on file)
# r is for read and t is for text. it also default parameter so you need not to mention it.

# To open a file on server
f = open("demofile.tx")
print(f.read())
# read() is a method to read contains of files.
# if file is in different place then specify path.

# you can also use with statement to open a file.
# using with statement.
with open("ddemofile.txt") as f:
    print(f.read())
# same as before just different way to write.
# also benefit is that with statement take care of file closing.

# close the file 
# use only if using conventional way of file reading and not using with statement
f = open("demolist.txt")
print(f.readline())
f.close()
# always close file after done working as sometimes changes not appear until you closed it.


# read only parts of the file.
# you can specifiy how many character should read() method should read in as parameter.
# Example :
with open("demofile.txt") as f:
    print(f.read(5))
# read only 5 characters.

# read lines using readline() method
# example : read first line of file
with open("demofile.txt") as f:
    print(f.readline())


# you can call readline() multiple times to read that many lines
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
# read top 2 line.

# or you can loop to ease the process line by line.
with open("demofile.txt")  as f:
    for x in f:
        print(x)


### File Write ###
# to writing in existing file.
# "a" - append - will append at the end of file
# "w" - write - will overwrite any existing content.

# example : for add content to existing file
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

# example : for overwriting the file
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())


# create a new file exist or not 
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists

# example : 
f = open("demofile.txt", "x") 
# new file is created.
# and if file exist error is raised.


### Delete file ###
# To delete a file you must import a module called OS, and then run its command
# like os.remove()

# Example to remove
import os
os.remove("demofile.txt")

# check if file exist
# to avoid getting error when removing the file, a check is must.
# example :
import os
if os.path.exists("demofile.txt"):
   os.remove("demofile.txt")
else :
   print("file does not exist")


# You can also delete a folder this way.
# but you can only remove empty folder.
# example : remove an entire directory
import os
os.rmdir("temp_folder")










