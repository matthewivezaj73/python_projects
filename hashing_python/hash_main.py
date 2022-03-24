#Importing the hashlib library.
import hashlib

#Asking the individual for their name.
your_name = input("Please enter your name here: ")
#Assigning a sha256 hash to a variable.
hashed_value = hashlib.sha256(your_name)
# creating a generic constructor
generic = hashlib.new('sha256')
print("Here is your name in a hashed value!")
print(named)