####################################################################################################
#
#   Date Written: 03/27/2023        By: Joseph P. Merten
#   Day 13:Checkers Game - Imports and NumPy Intro
#
#   What will the application do?
# DONE - 1 Point: The application prompts the user to enter a square board size between minimum of 4 and maximum of 16.
# The application prints out a random board where each cell is either empty or contains a red or black checker.
#
# Build Specifications:
# DONE - 1 point: This app must use two files, a main (called main.py) and a second one called checkers.py containing a function for generating a game board.
# Specifications for the checkers.py file:
# DONE - 1 point: The checkers.py file must import only the items from the numpy library required, using the “from” import construct.
# DONE - 1 point: The checkers.py file must contain a function called build_board which takes a parameter representing the size of the board; e.g. if 3 is passed in, the function will generate a 3x3 board. The function will then use numpy to populate each cell of the board randomly with one of the following strings: ‘Empty’, ‘Red’, ‘Black’. The function will then return the newly created board.
# DONE - 1 point: The checkers.py file must contain a function called get_count which takes two parameters: A board and a string of either Empty, Red, or Black. It will return how many of that item exists in the board.
# DONE - 1 point: The checkers.py file must check if it’s running as a main, and if so print out a message stating the file is not intended to be run as a main.
# Specifications for the main.py file:
# DONE - 1 point: The main.py file must import the entire checkers library.
# DONE - 1 point: The code must check if it’s running as main, and if so, call a function called game containing the main functionality, described next.
# DONE - 2 point: The game function will ask the user for the size of the board and will call the build_board function. It will then print out the full board (you can just print the variable out; no need for extra formatting). It will next print out how many empty cells, how many red cells, and how many black cells are in the board using a function from your checkers.py file.
#
####################################################################################################
#   imports
import checkers
import pandas as pd

####################################################################################################
#   Variables
board_size = 0

####################################################################################################
#   Functions
def game():
    """This function holds the main logic - building qand printing a checkerboard."""
    resize_flag = 'x'
    print("Welcome to GC checkers...")
    #   Get a valid board size between 4 and 64
    while resize_flag != 'n':
        board_size = int(Validator.validate_int("Please enter a board size betwee 4 and 64", 4, 64))
        #   generate the checker board
        checker_board = checkers.build_board(board_size)
        #   print the checker board
        print(checker_board)
        #   Get the counts for each color.
        print(" The count of Black: ", checkers.get_count(checker_board, "black"))
        print(" The count of Empty: ", checkers.get_count(checker_board, "empty"))
        print(" The count of Red: ", checkers.get_count(checker_board, "red"))
        #   get the counts in a smarer way
        g_counts = checkers.smart_count(checker_board)  # checkers.get_count(checker_board):
        print(sorted(g_counts.items()))
        print("pivoted board")
        # pd_checker_board = pd.DataFrame(checker_board)
        print(checker_board.transpose())
        resize_flag = Validator.validate_yn("Do you want to resize the board? (y/n)\n> ")

####################################################################################################
#   Classes
class Validator():
    def validate_yn(my_prompt):
        "This METHOD validates a yes/no response."
        my_resp = 'x'
        while my_resp != 'n' and my_resp != 'y':
            my_resp = input(my_prompt).lower()
            if my_resp != 'n' and my_resp != 'y':
                print("Invalid response, please enter 'y' or 'n'...")
        return my_resp
    def validate_int(my_prompt, min, max):
        """This method will display a message and validate that the response is an
        integer within the boundaries specified by min & max"""
        my_resp = min - 5   #force untrue...
        while not min <= my_resp <= max:
            print(my_prompt)
            my_resp = input()
            try:
                my_resp = int(my_resp)
            except:
                my_resp = min - 5
            if not min <= my_resp <= max:
                print("Invalid entry, please try again...")
        return my_resp

####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
if __name__ == "__main__":
   game()
