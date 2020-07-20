#! /usr/bin/env python

"""
6. Optional, connect to three networking devices one after the other.
Use send_command() to execute a show command on each of these devices.
Print this output to the screen.
"""

from getpass import getpass
from netmiko import Netmiko

password = getpass()

device1 = {
    "host": "sw01.test.domain",
    "username": "cisco",
    "password": password,
    "device_type": "cisco_s300",
}
device2 = {
    "host": "sw02.test.domain",
    "username": "cisco",
    "password": password,
    "device_type": "cisco_s300",
}
device3 = {
    "host": "sw03.test.domain",
    "username": "juniper",
    "password": password,
    "device_type": "juniper_junos",
}

for device in (device1, device2, device3):
    net_conn = Netmiko(**device)
    output = net_conn.send_command("show arp")
    net_conn.disconnect()

    print(device["host"])
    print(output)
