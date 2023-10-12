import random

def play_game():
    user_choice = input("Choose rock (r), scissor (s) or paper (p): ")
    options = ['r', 's', 'p']
    computer_choice = random.choice(options)

    print(f"Your choice: {user_choice}")
    print(f"Choose a computer: {computer_choice}")

    if user_choice == computer_choice:
        print("Draw!")
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        print("You win!")
    else:
        print("The computer won!")

play_game()
