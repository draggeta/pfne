#! /usr/bin/env python

"""
3.  Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS
version, serial number, and configuration register values.

Your output should look as follows:
OS Version: 15.4(2)T1
Serial Number: FTX0000038X
​Config Register: 0x2102
"""

import re

with open("show_version.txt") as f:
    file = f.read()

os_version = re.search(r"^Cisco .*?, Version (?P<os>\S+), .+$", file, flags=re.M)
serial_num = re.search(r"Processor board ID (?P<sn>\S+)$", file, flags=re.M)
config_reg = re.search(r"Configuration\s\S+\s\S+\s(?P<cr>\S+)$", file, flags=re.M)

print(
    f"OS Version: {os_version.group('os')}\n"
    f"Serial Number: {serial_num.group('sn')}\n"
    f"Config Register: {config_reg.group('cr')}\n"
)
