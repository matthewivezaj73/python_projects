#Importing the hashlib library.
import hashlib

#Assigning a sha256 hash to a variable.
named = hashlib.sha256()
# creating a generic constructor
generic = hashlib.new('sha256')
print("Here is your name in a hashed value!")
print(named)