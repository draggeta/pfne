#! /usr/bin/env python

"""
3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading
the lines until you have encountered the remote "System Name" and remote "Port id". Save these two
items into variables and print them to the screen. You should extract only the system name and port
id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
"""

with open("show_lldp_neighbors_detail.txt") as f:
    file = f.readlines()

# This is a lol way of doing it. More for illustation that it is possible.

output = []

i = 0
while i < len(file):
    line = file[i]
    if line.startswith("System Name:"):
        _, name = line.split(": ")
        output.append(name.strip())
    elif line.startswith("Port id:"):
        _, p_id = line.split(": ")
        output.append(p_id.strip())

    if len(output) == 2:
        break
    i += 1

print(output)
