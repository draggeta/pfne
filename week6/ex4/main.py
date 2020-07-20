#! /usr/bin/env python

"""
4. Use send_config_set() and send_config_from_file() to make
configuration changes.

The configuration changes should be benign. For example, on Cisco IOS
I typically change the logging buffer size.

As part of your program verify that the configuration change occurred
properly. For example, use send_command() to execute 'show run' and
verify the new configuration.
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
output = net_conn.send_config_set("logging buffered 999")
output += net_conn.send_config_from_file("config.txt")
output += net_conn.send_command("show run")
net_conn.disconnect()

print(output)
