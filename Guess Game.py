import random
print("Enter your name:")
name = str(input())
print("=============Welcome " + name + ", to guess the number game."
      "Am thinking of a number between 1 and 10========================")
print("------------------------------------------------------------------"
      "-----------------------------------------------------------")


def game_error_checker():#This function helps to check the game for errors
    try:
        game_engine()#this is where the game engine was called for the error checking
    print("Would you like to continue " + name)
    print("type Y for yes or N for No")
    print("Please " + name + " Kindly input integers only, between 1 & 10")
    play_game_func()


