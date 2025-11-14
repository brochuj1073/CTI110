# Justin Brochu
# 11/9/25
# P4HW1
# Scores enter by user. Using a loop. 
# Program Pseudocode

number_scores = int(input("How many scores do you want to enter? "))
scores = []
count = 1
while len(scores) < number_scores:
    score = float(input(f"Enter score #{count}: "))
    if 0 <= score <= 100:
        scores.append(score)
        count += 1
    else:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        

if scores:
    low_score = min(scores)
    scores.remove(low_score)
    average = sum(scores) / len(scores)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print("\n--------Results--------")
    print(f"Lowest Score  : {low_score:.1f}")
    print(f"Modified List : {scores}")
    print(f"Scores Average: {average:.2f}")
    print(f"Grade         : {grade}")
    print("-----------------------")
else:
    print("No scores were entered.")