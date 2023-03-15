import numpy as np


class TicTacToe:
    # crating Constructor for TicTacToe class
    def __init__(self):
        # creating a 3x3 matrix with all zeros
        self.board = np.zeros((3, 3))
        # creating a variable to store the current player
        self.current_player = 1

    # creating a method to check if the game is over
    def game_over(self):
        # checking if there is a winner
        for player in [1, 2]:
            # checking if the player has won vertically
            if np.any(np.all(self.board == player, axis=0)):
                return True
            # checking if the player has won horizontally
            if np.any(np.all(self.board == player, axis=1)):
                return True
            # checking if the player has won diagonally
            if np.all(np.diag(self.board) == player):
                return True
            if np.all(np.diag(np.fliplr(self.board)) == player):
                return True
        # checking if there is a tie
        if np.all((self.board == 0) == False):
            return True
        # if there is no winner or tie
        return False

    # craeting a method that prints the board
    def display_board(self):
        # creating a dictionary to map the values to X, O, and - based on the current player

        symbols = {1: "X", 2: "O", 0: "-"}
        # creating a string to store the board
        board_string = ""
        # looping through the rows
        for row in self.board:
            # looping through the columns
            for col in row:
                # adding the symbol to the board string
                board_string += symbols[col] + " "
            # adding a new line
            board_string += "\n"
        # printing the board
        print(board_string)

    # creating a method to get the current player

    def get_current_player(self):
        return self.current_player

    # creating a method to get the next player
    def get_next_player(self):
        if self.current_player == 1:
            return 2
        else:
            return 1

    # creating a method to make a move
    def move(self, row, col):
        # checking if the move is valid
        if self.board[row, col] == 0:
            # setting the value of the move
            self.board[row, col] = self.current_player
            # switching the current player
            self.current_player = self.get_next_player()
        else:
            print("Invalid move")

    # creating a method to get the winner
    def get_winner(self):
        # checking if there is a winner
        for player in [1, 2]:
            # checking if the player has won vertically
            if np.any(np.all(self.board == player, axis=0)):
                return player
            # checking if the player has won horizontally
            if np.any(np.all(self.board == player, axis=1)):
                return player
            # checking if the player has won diagonally
            if np.all(np.diag(self.board) == player):
                return player
            if np.all(np.diag(np.fliplr(self.board)) == player):
                return player
        # if there is no winner
        return None

    # creating a method to reset the game

    def reset(self):
        # creating a 3x3 matrix with all zeros
        self.board = np.zeros((3, 3))
        # creating a variable to store the current player
        self.current_player = 1

# creating a function to play the game


def play_game():
    # creating an instance of the TicTacToe class
    game = TicTacToe()
    # creating a variable to store the winner
    winner = None
    # looping until the game is over
    while not game.game_over():
        # displaying the board
        game.display_board()
        # getting the current player
        current_player = game.get_current_player()
        # asking the current player for a move
        print("Current Player: ", current_player)
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        # making the move
        game.move(row, col)
    # displaying the board
    game.display_board()
    # getting the winner
    winner = game.get_winner()
    # checking if there is a winner
    if winner is None:
        print("It's a tie")
    else:
        print("Player ", winner, " won")
    # asking the players if they want to play again
    answer = input("Do you want to play again? (y/n): ")
    # checking if the players want to play again
    if answer.lower() == "y":
        # resetting the game
        game.reset()
        # playing the game again
        play_game()
    else:
        print("Thanks for playing")


# playing the game
play_game()

# board = np.zeros((3, 3))
# print(board)
