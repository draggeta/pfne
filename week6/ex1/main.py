#! /usr/bin/env python

"""
1. Using Netmiko, establish a connection to a network device and print
out the device's prompt.
"""

from getpass import getpass
from netmiko import Netmiko

device = {
    "host": "sw01.test.domain",
    "username": "cisco",
    "password": getpass(),
    "device_type": "cisco_s300",
}

net_conn = Netmiko(**device)
net_conn.disconnect()

print(net_conn.find_prompt())
