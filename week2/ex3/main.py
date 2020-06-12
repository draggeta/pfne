#! /usr/bin/env python

"""
3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the
header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using
the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
"""

from pprint import pprint

with open("show_arp.txt") as f:
    file = f.readlines()

file = file[1:]
print("Unordered list:")
pprint(file)

file.sort()
print("Ordered list:")
pprint(file)

l_slice = file[:3]
l_str = "\n".join(l_slice)

with open("arp_entries.txt", mode="w") as f:
    f.write(l_str)
