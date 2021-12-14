#Creating a list of numbers.
my_numbers = [1,"One",2,"Two",3,"Three",4,"Four", 5, "Five", 6, "Six", 7, "Seven", 8, "Eight", 9, "Nine", 10, "Ten"]
#A for loop.
for numbers in my_numbers:
    #Checking if the value type is an integer.
    if type(numbers) is int:
        print("The number is in numerical form")
        #Adding a breakpoint
        breakpoint()
        #Handling the case where the user enters 1.
        if numbers == 1:
            print(f"The number is {my_numbers[0]}")
        #Adding a breakpoint
        breakpoint()
        #Handling the case where the user enters 2.
        elif numbers == 2:
            print(f"The number guessed is {my_numbers[2]}")
        #Handling the case where the user enters 3.
        elif numbers == 3:
            print(f"The number guessed is {my_numbers[4]}")
        #Handling the case where the user enters 4.
        elif numbers == 4:
            print(f"The number guessed is {my_numbers[6]}")
        #Handling the case where the user enters 5.
        elif numbers == 5:
            print(f"The number guessed is {my_numbers[8]}")
        #Handling the case where the user enters 6.
        elif numbers == 6:
            print(f"The number guessed is {my_numbers[10]}")
        #Handling the case where the user enters 6.
        elif numbers == 7:
            print(f"The number guessed is {my_numbers[6]}")
        #Handling the case where the user enters 6.
        elif numbers == 8:
            print(f"The number guessed is {my_numbers[8]}")
        #Handling the case where the user enters 6.
        elif numbers == 9:
            print(f"The number guessed is {my_numbers[10]}")
        #Handling the case where the user enters 6.
        elif numbers == 10:
            print(f"The number guessed is {my_numbers[9]}")
    elif numbers.isalpha():
        if numbers == "One":
            print(f"The number guessed is {my_numbers[]}")