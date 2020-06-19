#! /usr/bin/env python

"""
1. Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""

with open("show_vlan.txt") as f:
    file = f.readlines()

output = []

for line in file:
    if "VLAN" in line or "-" in line or line[0:5] != "     ":
        continue

    split_line = line.split()
    vlan_id = split_line[0]
    vlan_name = split_line[1]
    output.append((vlan_id, vlan_name))

print(output)
