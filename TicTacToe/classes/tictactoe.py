#Creating a class.
class tictactoe:
    #Creating a main function.
    def __init__(self,username,row,column):
        """
            Initializing username, row, and column.
        """
        self.username = username
        self.row = row
        self.column = column
    #Initializng the gameboard.
    def initializeGameboard(self):
        """
            A method to create the gameboard.
        """
        #Creating a gameboard.
        gameBoard = [4][4]
        #Assigning * to specific cells.
        gameBoard[0][0] = "*"
        gameBoard[0][2] = "*"