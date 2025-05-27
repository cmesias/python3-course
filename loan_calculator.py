
money_owed = float(input("How much money do you owe, in dollars? "))
apr = float(input("What is the annual percentage rate of the loan? "))
payment = float(input("How much will you pay off each month in dollars? "))
months = int(input("How many months do you want to see the results for? "))

monthly_rate = apr/100/12

for i in range(months):
    # Calculate interest to pay monthly
    interest_paid = money_owed*monthly_rate

    # Add in interest
    money_owed = money_owed + interest_paid

    # check if we paid off loan
    if money_owed - payment < 0:
        print(f"Your last payment is {money_owed}")
        print(f"You paid off the laon in {i+1} months!")
        break

    # Make payment
    money_owed = money_owed - payment

    print(f"Paid {payment} of which {interest_paid} was interest")
    print(f"Now I owe {money_owed}")