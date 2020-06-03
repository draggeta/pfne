#! /usr/bin/env python

'''5. You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS"
mappings. The output should look like following:

             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa

Two columns, 20 characters wide, data right aligned, a header column.
'''

from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1_list = mac1.split()
mac2_list = mac2.split()
mac3_list = mac3.split()

# Printing this with only one call to print()
print(f"{'IP ADDR':>20} {'MAC ADDRESS':>20}\n"
      f"{'-' * 20} {'-' * 20}\n"
      f"{mac1_list[1]:>20} {mac1_list[3]:>20}\n"
      f"{mac2_list[1]:>20} {mac2_list[3]:>20}\n"
      f"{mac3_list[1]:>20} {mac3_list[3]:>20}\n")
