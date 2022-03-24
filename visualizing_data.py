#Importing lib
import numpy as np
import pandas as pd
#Setting a flag.
not_done = False
#Starting a while loop.
while not not_done:
    #Asking the user what they would like to do.
    what_do = input("Please enter \'def\' if you would like to be tested over definitions.\nPlease enter \'ex_prob\' to go over example problems.\nPlease enter \'form\' to go over the formula for problems.")
    #Handling the case where the user wants to go over definitions.
    if what_do.lower() == "def":
        #Making a flag.
        not_choice = False
        #Testing for the choice.
        while not not_choice:
            #Asking the user to enter terms that they would like to be tested over.
            my_choice = input("Enter \'ungrouped data\' to be tested over that term.\nEnter \'grouped data\' "+
            "to be tested over that term.\nEnter \'frequency data\' to be tested over that term.\'Enter \'range\' to be tested over that term.\n"+
            "Enter \'relative frequency\' to be tested over that term.\nEnter \'cumulative frequency\' to be tested over that term.")
            #Handling the case where the user enters ungrouped data.
            if my_choice.lower() == "ungrouped data":
                print("Raw data or data that have not been summarized in any way.")
                not_choice = True
            elif my_choice.lower() == "grouped data":
                print("Data that has been organized into a frequency distribution.")
                not_choice = True
            elif my_choice.lower() == "frequency distribution":
                print("A summary of data presented in the form of class intervals and frequencies.")
                not_choice = True
            elif my_choice.lower() == "range":
                print("The difference between the largest and smallest numbers.")
                not_choice = True
            elif my_choice.lower() == "class midpoint":
                print("Midpoint of each class also called class mark.")
                not_choice = True
            elif my_choice.lower() == "relative frequency":
                print("The proportion of the total frequency that is in any given interval in a frequency distribution.")
                not_choice = True
            elif my_choice.lower() == "cumulative frequency":
                print("Running total of frequency through the classes of a frequency distribution.")
                not_choice = True
    #Handling the case where the user enters ex_prob.
    elif what_do.lower() == "ex_prob":
        #Giving the user direction
        print("I will display a set contianing the unique values and the number of counts.")
        #Creating a list of numbers.
        mortgage_arr = np.array([5.06,4.89,4.75,4.11,3.81,4.95,4.74,4.95,4.07,3.69,4.88,4.56,4.83,
        3.99,3.55,4.88,4.84,4.43,3.95,3.60,5.05,4.35,4.64,3.92,3.50,4.99,4.24,4.51,3.89,3.38,4.97,4.30,4.54,3.95,3.35,5.10,4.71,4.27,3.91,3.34])
        #Creating an array.
        mortgage_data = pd.Series(mortgage_arr)
        #Getting the count of the values.
        mortgage_count = mortgage_data.value_counts(sort=False)
        #Printing the count.
        print(mortgage_count)
        #Using numpy to create a frequncy table
        unique, counts = np.unique(mortgage_arr, return_counts=True)
        
        # print(np.asarray((unique, counts)))
        print("Displaying the frequency table below:")
        df = pd.DataFrame({'interval': ['A','A','A','B','B', 'B', 'B', 'C', 'D', 'D'],
                   'frequncy': [18, 18, 18, 19, 19, 20, 18, 18, 19, 19],
                   'Gender': ['M','M', 'F', 'F', 'F', 'M', 'M', 'F', 'M', 'F']})
        
    #Handling the case where the user enters form.
    elif what_do.lower() == "form":
        #Setting a flag to false.
        not_formula = False
        #Creating a while loop to test for input.
        while not not_formula:
            #Asking the user to enter a formula
            form_choice = input("Please enter \'class_width\' to view the formula for class width.")
            #Handling the case where the user enters class_width.
            if form_choice.lower() == "class_width":
                #Printing out the formula.
                print("Class Width = Range/Number of classes")