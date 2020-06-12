#! /usr/bin/env python

"""
1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file
contents to a variable. Print out the file contents to the screen. Also print out the type of the
variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file
contents using the .readlines() method. Print out the file contents to the screen. Also print out
the type of the variable (you should have a list at this point).
"""

# open and use the read method
f = open("show_version.txt")
file = f.read()

print("Normal open, read method output:")
print(file, "\n")
print("Normal open, read method type:")
print(type(file), "\n")

# close the file
f.close()

# open with context manager
with open("show_version.txt") as f:
    ctx_file = f.readlines()

print("Context open, readlines method output:")
print(ctx_file, "\n")
print("Context open, readlines method type:")
print(type(ctx_file), "\n")
