import os
expenses = []

print("Enter an expense otherwise enter 'done' when finished.")

while True:
    response = input("Enter an expense: ")
    response = response
    
    if response.isdigit():
        expenses.append(float(response))
    elif response=="list":
        print(expenses)
    elif response=="done":
        break


total = sum(expenses)

print(f"Your Total is ${total} dollars!")