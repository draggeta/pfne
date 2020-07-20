#! /usr/bin/env python

"""
3. Similar to lesson3, exercise4 write a function that normalizes a MAC
address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from
'00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should
return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words,
this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working
properly.
"""

import re


def norm_mac(mac_address):
    mac_list = []
    if re.match(r"([\da-fA-F]{4}\.?){3}", mac_address):
        mac_split = mac_address.split(".")
        mac_list.extend([y for x in mac_split for y in [x[0:2], x[2:4]]])
    elif re.match(r"^([\da-fA-F]{2}-){5}([\da-fA-F]{2})$", mac_address):
        mac_list = mac_address.split("-")
    output = ":".join(mac_list).upper()

    return output


print(norm_mac("0000.aaaa.bbbb"))
print(norm_mac("00-00-aa-aa-bb-bb"))
