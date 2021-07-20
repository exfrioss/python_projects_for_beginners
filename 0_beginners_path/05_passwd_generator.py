"""
Pyhton program to generate password.
To write a Pyhton program to create a password, declare a strings of numbers + uppercase + lowercase + special characters.
Take a random sample of the string of a length given by the user.
"""

import random
pass_len = int(input('Enter the lenght of password: '))
strings = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passwd = "".join(random.sample(strings, pass_len))
print(passwd)