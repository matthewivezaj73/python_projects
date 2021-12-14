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
            print(f"The number guessed is {my_numbers[12]}")
        #Handling the case where the user enters 6.
        elif numbers == 8:
            print(f"The number guessed is {my_numbers[14]}")
        #Handling the case where the user enters 6.
        elif numbers == 9:
            print(f"The number guessed is {my_numbers[16]}")
        #Handling the case where the user enters 6.
        elif numbers == 10:
            print(f"The number guessed is {my_numbers[18]}")
    elif numbers.isalpha():
        #Adding a breakpoint
        breakpoint()
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "O":
            print(f"The number guessed is {my_numbers[1]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "T" and numbers[1] == "w":
            print(f"The number guessed is {my_numbers[3]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "T" and numbers[1] == "h":
            print(f"The number guessed is {my_numbers[5]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "F":
            print(f"The number guessed is {my_numbers[7]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "F" and numbers[1] == "i":
            print(f"The number guessed is {my_numbers[9]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "S" and numbers[0] == "i":
            print(f"The number guessed is {my_numbers[11]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "S" and numbers[1] == "e":
            print(f"The number guessed is {my_numbers[13]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "E":
            print(f"The number guessed is {my_numbers[15]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "N":
            print(f"The number guessed is {my_numbers[17]}")
        #Handling the case where the user enters One.
        if type(numbers) is str and numbers[0] == "T":
            print(f"The number guessed is {my_numbers[19]}")
    