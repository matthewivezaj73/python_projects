#Importing library.
from numpy.random import randn
#Creating a dictionaru.
data = {my_var : randn() for my_var in range(7)}
#A for loop to access each line.
for line in data:
    print(line)