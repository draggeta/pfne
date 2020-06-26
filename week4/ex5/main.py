#! /usr/bin/env python

"""
5. Read the 'show_ipv6_intf.txt' file.

From this file, use Python regular expressions to extract the two IPv6 addresses.

The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64

Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of the
literal characters in the IPv6 address.

From this, create a list of IPv6 addresses that includes only the above two addresses.

Print this list to the screen.
"""

import re

with open("show_ipv6_intf.txt") as f:
    file = f.read()

ip_v6 = re.search(
    r"(?<=IPv6 address:).*?([a-f\d:]+\/\d+).*?([a-f\d:]+\/\d+).*?(?=IPv6 subnet)",
    file,
    flags=re.DOTALL,
)

print(f"IPv6 addresses:\n{ip_v6.group(1)}\n{ip_v6.group(2)}\n")
