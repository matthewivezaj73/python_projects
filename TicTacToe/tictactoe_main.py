#Matthew Ivezaj
#6/20/2022
#Tic Tac Toe
#Importing tictactoe from the class file, tictactoe.
from classes.tictactoe import tictactoe
#Creating a class object.
new_tictactoe = tictactoe('Monty', 5, 5)
#Setting flag to false.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user if they would like to enter an X or an O.
    user_choice = input("Please enter your token (X or O):\t")
    #Printing out the gameboard.
    print(new_tictactoe.initializeGameboard())