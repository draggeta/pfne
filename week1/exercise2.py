#! /usr/bin/env python

"""
2. Prompt a user to enter in an IP address from standard input. Read the IP
address in and break it up into its octets. Print out the octets in decimal,
binary, and hex.

Your program output should look like the following:

​ $ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the
column.
"""

from __future__ import print_function, unicode_literals

import ipaddress
import sys

# Read input, first option is used for Py2, the except is used for Py3.
try:
    ip_addr = raw_input("Please enter an IP address: ")
except NameError:
    ip_addr = input("Please enter an IP address: ")

# Validate the input to make sure it's an IPv4 address. Overkill for now, just
# for illustration.
try:
    ipaddress.IPv4Address(ip_addr)
except ipaddress.AddressValueError:
    sys.exit(f"The specified IP address {ip_addr} is not a valid IPv4 address")

# Would be better with a loop, but that concept is nog explained up to this
# point.
oct1 = int(ip_addr.split(".")[0])
oct2 = int(ip_addr.split(".")[1])
oct3 = int(ip_addr.split(".")[2])
oct4 = int(ip_addr.split(".")[3])

# Works in Py3 and Py2
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(oct1, oct2, oct3, oct4))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(oct1), bin(oct2), bin(oct3), bin(oct4)))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(oct1), hex(oct2), hex(oct3), hex(oct4)))

# This is the preferred way from Py3.6 on.
# print(f"{'Octet1':^15}{'Octet2':^15}{'Octet3':^15}{'Octet4':^15}")
# print(f"{'-' * 60}")
# print(f"{oct1:^15}{oct2:^15}{oct3:^15}{oct4:^15}")
# print(f"{bin(oct1):^15}{bin(oct2):^15}{bin(oct3):^15}{bin(oct4):^15}")
# print(f"{hex(oct1):^15}{hex(oct2):^15}{hex(oct3):^15}{hex(oct4):^15}")

# using the b and x formatting doesn't add 0b or 0x to the output.
# print(f"{'Octet1':^15}{'Octet2':^15}{'Octet3':^15}{'Octet4':^15}")
# print(f"{'-' * 60}")
# print(f"{oct1:^15}{oct2:^15}{oct3:^15}{oct4:^15}")
# print(f"{oct1:^15b}{oct2:^15b}{oct3:^15b}{oct4:^15b}")
# print(f"{oct1:^15x}{oct2:^15x}{oct3:^15x}{oct4:^15x}")
