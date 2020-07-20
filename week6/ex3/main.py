#! /usr/bin/env python

"""
3. Find a command on your device that has additional prompting. Use
send_command_timing to send the command down the SSH channel. Capture
the output and handle the additional prompting.
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
output = net_conn.send_command_timing("write memory")

if "Overwrite file" in output:
    output += net_conn.send_command_timing("Y\n")

net_conn.disconnect()

print(output)
