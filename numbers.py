#Creating a list of numbers.
my_numbers = [1,"One",2,"Two",3,"Three",4,"Four", 5, "Five", 6, "Six", 7, "Seven", 8, "Eight", 9, "Nine", 10, "Ten"]
#A for loop.
for numbers in my_numbers:
    if numbers.isdigit():
        print("The number is in numerical for")
        #Handling the case where the user enters 1.
        if numbers == 1:
            print(f"The number is {my_numbers[0]}")
        #Handling the case where the user enters 2.
        elif numbers == 2:
            print(f"The number guessed is {my_numbers[1]}")
        #Handling the case where the user enters 3.
        elif numbers == 3:
            print(f"The number guessed is {my_numbers[2]}")
        #Handling the case where the user enters 4.
        elif numbers == 4:
            print(f"The number guessed is {my_numbers[3]}")
        #Handling the case where the user enters 5.
        elif numbers == 5:
            print(f"The number guessed is {my_numbers[4]}")
        #Handling the case where the user enters 6.
        elif numbers == 6:
            print(f"The number guessed is {my_numbers[5]}")