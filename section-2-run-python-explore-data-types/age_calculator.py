# resources: https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/

### more efficient version + my own else statement
age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10

if years == 0:
    print(f"You are {decades} decades old!")
else:
    print(f"You are {decades} decades and {years} years old!")

### my version
# age = int(input("How old are you?\n"))
# if age >= 100:
#     decades_age = age/10
#     # check if trailing decimal is a 0, then just show whole number
#     if decades_age%1 == 0:
#         print(f"You are {int(decades_age)} decades old! Wow!")
#     # else show trailing decimal as 'X years old'
#     else:
#         # user modulo operator (%), numberator / denominator
#         # so an age of 202 would give us a remainder of 2
#         remainder_years_old = age % 10
#         print(f"You are {int(decades_age)} decades and {remainder_years_old} old, wowee!")
# else:
#     print(f"You are {age} years old!")