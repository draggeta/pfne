#! /usr/bin/env python

"""
1. Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper',
then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for
'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network
device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and
values.
"""


device = {
    "ip_addr": "10.0.0.1",
    "vendor": "cisco",
    "username": "sa_automation",
    "password": "P@$$w0rd!",
}

print(f"IP address: {device['ip_addr']}")

if device["vendor"] == "cisco":
    device["platform"] = "ios"
elif device["vendor"] == "juniper":
    device["platform"] = "junos"

bgp_fields = {"bgp_as": 64532, "peer_as": 65123, "peer_ip": "10.0.0.2"}

device.update(bgp_fields)

i = 1
print("-" * 30)
for key in device:
    print(f"Key {i:0>2}: {key}")
    i += 1

i = 1
print("-" * 30)
for k, v in device.items():
    print(f"Key/Value {i:0>2}: {k:<10} {v:<10}")
    i += 1
