#! /usr/bin/env python

"""
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to
add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the
last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the
list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in
the list.
"""

ip_addrs = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.5"]

# append and extend
ip_addrs.append("10.0.0.6")
ip_addrs.extend(["10.0.0.7", "10.0.0.8"])

# list concatenation
ip_addrs = ip_addrs + ["10.0.0.9", "10.0.0.10"]

print("All IPs:\n", ip_addrs)
print("First IP:\n", ip_addrs[0])
print("Last IP:\n", ip_addrs[-1])

ip_addrs.pop(0)
ip_addrs.pop()

ip_addrs[0] = "2.2.2.2"
print("First IP:\n", ip_addrs[0])
