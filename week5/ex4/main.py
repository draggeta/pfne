#! /usr/bin/env python

"""
4. Copy your solution from exercise3 to exercise4. Add an 'import pdb'
and pdb.set_trace() statement outside of your function (i.e. where you
have your function calls).

Inside of pdb, experiment with:
Listing your code.
Using 'next' and 'step' to walk through your code. Make sure you
understand the difference between next and step.
Experiment with 'up' and 'down' to move up and down the code stack.
Use p <variable> to inspect a variable.
Set a breakpoint and run your code to the breakpoint.
Use '!command' to change a variable (for example !new_mac = [])
"""

import re
import pdb


def norm_mac(mac_address):
    mac_list = []
    if re.match(r"([\da-fA-F]{4}\.?){3}", mac_address):
        mac_split = mac_address.split(".")
        mac_list.extend([y for x in mac_split for y in [x[0:2], x[2:4]]])
    elif re.match(r"^([\da-fA-F]{2}-){5}([\da-fA-F]{2})$", mac_address):
        mac_list = mac_address.split("-")
    output = ":".join(mac_list).upper()

    return output


pdb.set_trace()

print(norm_mac("0000.aaaa.bbbb"))
print(norm_mac("00-00-aa-aa-bb-bb"))
