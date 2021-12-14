#Creating a list of numbers.
my_numbers = [1,"One",2,"Two",3,"Three",4,"Four", 5, "Five", 6, "Six", 7, "Seven", 8, "Eight", 9, "Nine", 10, "Ten"]
#A for loop.
for numbers in my_numbers:
    if numbers.isdigit():
        print("The number is in numerical for")
        #Handling the case where the user enters 1.
        if numbers == 1:
            print(f"The number is {my_numbers[0]}")
        elif numbers == 2:
            print(f"The number guessed is {my_numbers[1]}")