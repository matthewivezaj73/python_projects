#Importing numpy lib.
import numpy as np
#Creating a dictionary.
data = {my_var : np.random.rand() for my_var in range(7)}
#Printing each line out of the dictionary.
for line in data:
    print(line)