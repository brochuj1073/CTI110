# Justin Brochu
# 10/10/25
# travel
# Program to calculate travel expenses


print("This program calculates and displays travel expenses")
print()
print("Enter Budget:", end="")
Budget= float(input())
print()
print("Enter your travel destination:", end="")
destination = (input())
print()
print("How much do you think you will spend on gas?", end="")
gas= float(input())
print()
print("Approximately, how much will you need for accomodation/hotel?", end="")
hotel= float(input())
print()
print("Last, how much do you need for food?", end=""), 
food= float(input())
print()
print("------------Travel Expenses------------")

InitialBudget = Budget
location = destination
Fuel = gas
Accomodation = hotel
Food = food

print(f"Location:       {location:}")
print(f"Initial Budget: ${InitialBudget:.2f}")

print(f"Fuel:           ${Fuel:.2f}")

print(f"Accomodation:   ${Accomodation:.2f}") 

print(f"Food:           ${Food:.2f}")

print("----------------------------------")
outcome= Fuel + Accomodation + Food 
remaining= InitialBudget - outcome
print()
print(f"Remaining Balance: ${remaining:.2f}")





