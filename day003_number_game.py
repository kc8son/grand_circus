####################################################################################################
#
#   Date Written: 03/02/2023        By: Joseph P. Merten
#   Day 3 - NUMBER ANALYZER - Decision Maker
#
####################################################################################################
#   imports

#   variables

#   main routine
player_name = input("Welcome to the python game, what is your name? ")
player_entry = int(input(f"{player_name}, Please enter an integer between 1 and 100 inclusive (enter 0 to quit: "))
while (1<= player_entry <= 100):
    # 1 Point: If the integer entered is odd and less than 60, print the number entered and “Odd and less than 60.”
    if (player_entry%2 == 1) and (player_entry < 60):
        print(f"{player_name}, {player_entry} is: Odd and less than 60")
    # 1 Point: If the integer entered is even and in the inclusive range of 2 to 24, print “Even and less than 25.”
    if (player_entry%2 == 0) and (player_entry <= 24):
        print(f"{player_name}, {player_entry} is: Even and less than 25.")
    # 1 Point: If the integer entered is even and in the inclusive range of 26 to 60, print “Even and between 26 and 60 inclusive.”
    if (player_entry%2 == 0) and (26 <= player_entry <= 60):
        print(f"{player_name}, {player_entry} is: Even and between 26 and 60 inclusive.")
    # 1 Point: If the integer entered is even and greater than 60, print the number entered and “Even and greater than 60.”
    if (player_entry%2 == 0) and (player_entry > 60):
        print(f"{player_name}, {player_entry} is: Even and greater than 60.")
    # 1 Point: If the integer entered is odd and greater than 60, print the number entered and “Odd and greater than 60.”
    if (player_entry%2 == 1) and (player_entry > 60):
        print(f"{player_name}, {player_entry} is: Odd and greater than 60.")
    player_entry = int(input(f"{player_name}, Please enter an integer between 1 and 100 inclusive (enter 0 to quit: "))