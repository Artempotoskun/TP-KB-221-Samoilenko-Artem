import random

def play_game():
    user_choice = input("Choose rock (r), scissor (s) or paper (p): ")
    options = ['r', 's', 'p']
    computer_choice = random.choice(options)

    print(f"Your choice: {user_choice}")
    print(f"Choose a computer: {computer_choice}")

    if user_choice == computer_choice:
        print("Draw!")
        return
    
    user_win = True

    if user_choice == 'r' and computer_choice == 'p':
        user_win = False
    elif user_choice == 's' and computer_choice == 'r':
        user_win = False
    elif user_choice == 'p' and computer_choice == 's':
        user_win = False
    
    if user_win:
        print("User win")
    else:
        print("Computer win")


play_game()
