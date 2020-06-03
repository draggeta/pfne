#! /usr/bin/env python

'''4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
'''

from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version_stripped = show_version.strip()
# print(f"Stripped 'show version' output: {show_version_stripped}\n")

_, model, serial_no = show_version_stripped.split()

print(f"Vendor is Cisco?: {'cisco' in model.lower()}")
print(f"Model is 881?: {'881' in model}")
print(f"Model: {model}\nSerial Number: {serial_no}")
