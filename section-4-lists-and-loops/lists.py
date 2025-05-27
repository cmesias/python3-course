import os

acronyms = []

def print_all_acronyms():
    for idx, item in enumerate(acronyms):
        print(f"Acronym {idx}: {item}")

def contains_numbers(str):
    return any(char.isdigit() for char in str)

def contains(str, sub_str):
    if sub_str in str:
        return True
    else:
        return False

def print_enter_to_continue():
    print("\n==============================")
    print("    Press Enter to continue   ")
    print("==============================")
    input()

game = True
while game:

    # clear console every loop
    os.system("cls")

    # get user input
    result = input("Enter a new acronym to add to database: ")

    # check if input has numbers
    has_numbers = contains_numbers(result)

    # continue if user input doesn't have numbers
    if not has_numbers:
        # check if user input already exists in acronym database
        if result =="list":
            print("\nList of acronyms in database:")
            print_all_acronyms()

            response = input("Remove items by it's index: 'delete X'")

            # check if starts with '/delete '
            if response.startswith("/delete ")
                del acronyms[]




            print_enter_to_continue()
        elif result =="clear":
            os.system("cls")
        # User wants to exist
        elif result =="exit":
            print("exiting...")
            print_enter_to_continue()
            break
        # Check for errors
        elif result =="":
            print("\nEmpty input. Please enter some letters (A-Z).")
        # Check if acronym already exists
        elif result in acronyms:
            print(f"\nAcronym '{result}' exists in database, please select a new one.")
            print_enter_to_continue()
        # Add acronym to database
        elif result not in acronyms:
            print(f"\nAdding acronym '{result}' to database...")
            acronyms.append(result)
            print(f"Finished!")
            print_enter_to_continue()
        # else add the acronym
        else:
            print("Unknown command.")
            break
    else:
        print("Please enter only A-Z characters.")
        print_enter_to_continue()
