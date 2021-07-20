# init the variable "phrase_input" to assign the value of input function
phrase_input = input("Enter a phrase: ")
# In this part we initialize the "text" variable and split the input value
text = phrase_input.split()
# Here we initialize the "a" variable. The "a" variable will be accumulate de 
# first letter of "text" in upper case
a = ' '
# we walk into each character in the text with for loop
for i in text:
    # The "a" variable will be accumulate de first (i[0]) letter of "text" in upper case
    a = a+i[0].upper()

print(a)