import random
char_lower = 'abcdefghijklmnopqrstuvwxyz'
char_upper = char_lower.upper()
numbers = "0123456789"
symbols = "[]{}()*;/,._-"
all = char_lower + char_upper + numbers + symbols
length = 16
password = "".join(random.sample(all, length))
print(password)
