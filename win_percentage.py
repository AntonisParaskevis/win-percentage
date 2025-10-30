# Prompt the user to enter the name of a team
team = input("Enter the name of a team\n")

while True:
    # Prompt the user to enter the number of wins
    wins_num = input("Enter the number of wins\n")
    
    # Check whether the user's input is valid (in this case, zero or a positive integer). If the user has entered a letter, a punctation mark, a symbol, a non-integer number or a negative number, prompt the user to enter a valid input
    if not wins_num.isdigit() or int(wins_num) < 0:
        print("Invalid entry, please enter zero, or an integer greater than zero.")
        continue
    else:
        # Convert the user's input into an integer, as the input itself is a string by default
        wins_num = int(wins_num)
        break

# Same for the number of losses
while True:
    loses_num = input("Enter the number of losses\n")
    
    if not loses_num.isdigit() or int(loses_num) < 0:
        print("Invalid entry, please enter zero, or an integer greater than zero.")
        continue
    else:
        loses_num = int(loses_num)
        break

# If no matches have been played, the win percentage cannot be calculated. We would have to calculate 0/0, which is not possible
if wins_num == 0 and loses_num == 0:
    # Display a message saying that no matches have been played yet
    print("No matches have been played yet")
else:
    # Calculate the team's win percentage, using the user's input
    win_percentage = (wins_num / (wins_num + loses_num)) * 100
        
    # Display the team's win percentage, rounded to 2 decimals
    print(team + " have won " + str(round(win_percentage, 2)) + "% of their matches.")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")