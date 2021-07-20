"""
Email slicer:
An email slicer is a very useful program for separating the username and domain name of an email address.

To create an email slicer with Python, our task is to write a program that can retrive the username and the
domain name of the email. For example: 'frioss@domain.com'.

So we need to divide the email into two strings using '@' as the seperator.
Let's see how to separate the email and domain name with Pyhton.
"""

def email_slicer_slicing(email):
    username = email[:email.index('@')]
    domain_name = email[email.index('@')+1:]
    format_message = (f"Your user name is: '{username}' and your domain is '{domain_name}'")
    print(format_message)
    
    
def email_slicer_split(email):
    data = email.split('@')
    username = data[0]
    domain_name = data[1]
    format_message = (f"Your user name is: '{username}' and your domain is '{domain_name}'")
    print(format_message)

email = input("Enter your Email: ").strip()
email_slicer_slicing(email)
email_slicer_split(email)