
import random
import os

game = True
computer_wins = 0
user_wins = 0
ties = 0

def reset_game():
    global computer_wins
    global user_wins
    global ties
    computer_wins = 0
    user_wins = 0
    ties = 0

def PlayGame():
    global game
    global computer_wins
    global user_wins
    global ties
    result = "Game Start"
    choices = ['', 'Rock', 'Paper', 'Scissors', 'reset', 'exit']

    while game:
        # clear console every loop
        os.system('clear' if os.name == 'posix' else 'cls')
        print("###########################################")
        print("")
        print(f"User Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")
        print(f"Ties: {ties}")
        print("")
        print("###########################################")

        print("\n\nPlease enter a number (1-4):")
        print("1. Rock\n2. Paper\n3. Scissors\n4. reset game\n5. exit game\n") 
        user_input = input("")
        print("")

        # valid if input is a digit
        if user_input.isdigit():

            # convert user input to int
            int_choice = int(user_input)

            # validate input is 1-4 only
            if int_choice >= 1 and int_choice <= 5:

                # set user choice
                user_choice = choices[int_choice]

                # set computer choice
                computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

                # Reset Game
                if user_choice=='reset':
                    response = input("Are you sure you want to Reset the game? (Y/n): ")
                    if response[0]=="Y" or response[0] =="y":
                        reset_game()
                    else:
                        # do nothing
                        print("Continuing game. Press Enter to continue....")
                        input("")
                # Quit Game
                elif user_choice=='exit':
                    response = input("Are you sure you want to Quit the game? (Y/n): ")
                    if response[0]=="Y" or response[0] =="y":
                        return
                    else:
                        # do nothing
                        print("Continuing game. Press Enter to continue....")
                        input("")
                # Run game
                else:
                    if user_choice==computer_choice:
                        result = "TIE"
                        ties+=1
                    elif computer_choice=="Rock" and user_choice=="Paper":
                        result = "You Win!"
                        user_wins+=1
                    elif computer_choice=="Paper" and user_choice=="Scissors":
                        result = "You Win!"
                        user_wins+=1
                    elif computer_choice=="Scissors" and user_choice=="Rock":
                        result = "You Win!"
                        user_wins+=1
                    else:
                        result = "You Lose!"
                        computer_wins+=1

                    # Winner/Loser screen
                    print(f"\nResult: {result}")
                    print(f"You - {user_choice}")
                    print(f"Computer - {computer_choice}")
                    print("\n")
                    input("Press Enter to continue...")
            else:
                print("Please enter a valid number (1-4).\n")
                input("Press Enter to continue...")
        else:
            print("Invalid input. Please enter a numerical value (1-4)\n")
            input("Press Enter to continue...")

PlayGame()