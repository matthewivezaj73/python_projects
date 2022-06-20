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
        gameBoard[0][4] = "*"
        gameBoard[2][0] = "*"
        gameBoard[2][2] = "*"
        gameBoard[2][4] = "*"
        gameBoard[4][0] = "*"
        gameBoard[4][2] = "*"
        gameBoard[4][4] = "*"
        #Assigning _ to specific cells.
        gameBoard[1][0] = "_"