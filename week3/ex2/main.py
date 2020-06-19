#! /usr/bin/env python

"""
2. Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this
file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a
separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the
string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then
print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have
found both of these devices, 'break' out of the for loop.
"""

with open("show_arp.txt") as f:
    file = f.readlines()

def_gw = False
arista = False

for line in file:
    if not line.startswith("Internet"):
        continue
    split_lines = line.split()
    ip_addr = split_lines[1]
    mac_addr = split_lines[3]

    if ip_addr == "10.220.88.1":
        print(f"Default gateway IP/Mac: {ip_addr} {mac_addr}")
        def_gw = True
    elif ip_addr == "10.220.88.30":
        print(f"Arista3 IP/Mac is: {ip_addr} {mac_addr}")
        arista = True

    if def_gw and arista:
        break
