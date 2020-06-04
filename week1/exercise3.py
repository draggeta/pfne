#! /usr/bin/env python

"""
3.   Create three different variables the first variable should use all
lower case characters with underscore ( _ ) as the word separator. The second
variable should use all upper case characters with underscore as the word
separator. The third variable should use numbers, letters, and underscore, but
still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are
unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
"""

from __future__ import print_function, unicode_literals

ip_addr = "dead:beef::"
MY_IP_OK = "face::b00c"
your_99_ip = "9009::1e"

# Splitting it up like this keeps the lines under the 80 character PEP8 limit.
# It's ugly, but good for the course.
print(
    f"IPv6 address '{ip_addr}' and '{MY_IP_OK}' are equal: "
    f"{ip_addr == MY_IP_OK}"
)
print(
    f"IPv6 address '{ip_addr}' and '{your_99_ip}' are not equal: "
    f"{ip_addr != your_99_ip}"
)
