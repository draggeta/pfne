#! /usr/bin/env python

"""
2. Create three separate lists of IP addresses. The first list should be the IP addresses of the
Houston data center routers, and it should have over ten RFC1918 IP addresses in it (including some
duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers, and it should have at
least eight RFC1918 IP addresses (including some addresses that overlap with the Houston data
center).

The third list should be the IP addresses of the Chicago data center routers, and it should have at
least eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP
addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago
"""

ip_houston_list = [
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.3",
    "10.9.4.1",
    "10.9.4.2",
    "10.9.4.3",
    "10.15.100.1",
    "10.15.100.2",
    "10.15.100.3",
    "10.0.0.1",
    "10.9.4.2",
    "10.15.100.3",
]
ip_atlanta_list = [
    "10.0.0.2",
    "10.9.4.3",
    "10.15.100.1",
    "10.64.64.1",
    "10.64.64.2",
    "10.64.64.3",
    "10.92.3.1",
    "10.92.3.2",
    "10.92.3.3",
]
ip_chicago_list = [
    "10.0.0.3",
    "10.9.4.1",
    "10.15.100.2",
    "10.64.64.1",
    "10.92.3.2",
    "10.128.254.1",
    "10.128.254.2",
    "10.128.254.3",
    "10.140.29.1",
    "10.140.29.2",
    "10.140.29.3",
]

ip_houston_set = set(ip_houston_list)
ip_atlanta_set = set(ip_atlanta_list)
ip_chicago_set = set(ip_chicago_list)

print(
    f"Duplicates between Houston and Atlanta: {ip_houston_set.intersection(ip_atlanta_set)}\n"
    f"Duplicates between all sites: {ip_houston_set.intersection(ip_atlanta_set).intersection(ip_chicago_set)}\n"
    f"Uniques in Chicago site: {ip_chicago_set.difference(ip_atlanta_set).difference(ip_houston_set)}\n"
)
