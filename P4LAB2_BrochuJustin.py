# Justin Brochu
# 11/2/25
# P4LAB2
# displays information to users using loops

go_again = "yes"
while go_again != "no":

 person_num = int(input("\nEnter an Integer: "))
 if person_num >= 0:
    for num in range(1,13):
        print(f"{person_num} * {num} = {person_num * num}")
 else: 
    print("\nThis program does not handle negative numbers")
 
 go_again = input("\nWould you like to run the program again? ")
print("\nExiting Program....")
