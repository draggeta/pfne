#! /usr/bin/env python

"""
1a. Create an ssh_conn function. This function should have three
parameters: ip_addr, username, and password. The function should print
out each of these three variables and clearly indicate which variable
it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named
arguments.


1b. Expand on the ssh_conn function from exercise1 except add a fourth
parameter 'device_type' with a default value of 'cisco_ios'. Print all
four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the
device_type

Create a dictionary that maps to the function's parameters. Call this
ssh_conn2 function using the **kwargs technique.
"""

def ssh_conn(ip_addr, username, password):
    print(
        f"ip_addr: {ip_addr}\n"
        f"username: {username}\n"
        f"password: {password}\n"
    )

def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print(
        f"ip_addr: {ip_addr}\n"
        f"username: {username}\n"
        f"password: {password}\n"
    )

print("--- 1 - Positional arguments ---")
ssh_conn("10.0.0.1", "admin", "password")
print("--- 1 - Named arguments ---")
ssh_conn(ip_addr="10.0.0.2", username="root", password="welcome")
print("--- 1 - Mixed arguments ---")
ssh_conn("10.0.0.3", password="mixed", username="superuser")

print("--- 2 - Default value ---")
ssh_conn2("10.0.0.1", "admin", "password")
print("--- 2 - Specified value ---")
ssh_conn2("10.0.0.2", "manager", "password", "junos")
