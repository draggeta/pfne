#! /usr/bin/env python

"""
2. Use send_command() to send a show command down the SSH channel.
Retrieve the results and print the results to the screen.
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
output = net_conn.send_command("show arp")
net_conn.disconnect()

print(output)
