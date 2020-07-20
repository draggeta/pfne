#! /usr/bin/env python

"""
5. Optional, use send_command() in conjunction with ntc-templates to
execute a show command. Have TextFSM automatically convert this show
command output to structured data.
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
# doesn't work on s300, oh well...
output = net_conn.send_command("show arp", use_textfsm=True)
net_conn.disconnect()

print(output)
