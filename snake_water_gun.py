import random

# ---------------------------------------------
# Snake Water Gun Game
# Author : Vivek Kumar
# Language : Python
#
# Rules:
# Snake (1) drinks Water (0)
# Water (0) defeats Gun (-1)
# Gun (-1) kills Snake (1)
# ---------------------------------------------

# Dictionary to map numbers to choice names
choice_name = {
    1: "Snake",
    0: "Water",
    -1: "Gun"
}

# Computer randomly selects one option
computer_choice = random.choice([1, 0, -1])

# Display instructions to the user
print("========== Snake Water Gun Game ==========")
print("Choose an option:")
print("1  -> Snake")
print("0  -> Water")
print("-1 -> Gun")

# Take input from the user
user_choice = int(input("\nEnter your choice: "))

# Validate user input
if user_choice not in choice_name:
    print("\n Invalid choice! Please enter only 1, 0, or -1.")
    exit()

# Display both choices
print("\n----------- Result -----------")
print(f"Your Choice     : {choice_name[user_choice]}")
print(f"Computer Choice : {choice_name[computer_choice]}")

# Decide the winner
if computer_choice == user_choice:
    print("\n Match Draw!")

elif computer_choice == 1 and user_choice == 0:
    print("\n Computer Wins!")

elif computer_choice == 1 and user_choice == -1:
    print("\n You Win!")

elif computer_choice == 0 and user_choice == 1:
    print("\n You Win!")

elif computer_choice == 0 and user_choice == -1:
    print("\n Computer Wins!")

elif computer_choice == -1 and user_choice == 0:
    print("\n Computer Wins!")

elif computer_choice == -1 and user_choice == 1:
    print("\n You Win!")

print("\nThank you for playing! 😊")