#! /usr/bin/env python

"""
5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and
last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""

with open("show_ip_bgp_summ.txt") as f:
    file = f.readlines()

first_line = file[0]
last_line = file[-1]

bgp_as = first_line.split()[-1]
bgp_peer_ip = last_line.split()[0]

print(f"{'AS number':9} {'BGP peer IP address':19}\n" f"{bgp_as:>9} {bgp_peer_ip:>19}")
