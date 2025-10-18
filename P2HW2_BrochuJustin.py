# Justin Brochu
# 10/11/25
# P2HW2
# Having students input grades
# program Pseudocode (detail algorithm)

grades = []

grades.append(float(input("Enter grade for Module 1:   ")))
grades.append(float(input("Enter grade for Module 2:   ")))
grades.append(float(input("Enter grade for Module 3:   ")))
grades.append(float(input("Enter grade for Module 4:   ")))
grades.append(float(input("Enter grade for Module 5:   ")))
grades.append(float(input("Enter grade for Module 6:   ")))

print("\n------------Results------------")

lowest_score = min(grades)
highest_score = max(grades)
sum_score = sum(grades)
all_score = len(grades)
ave_score = sum_score / all_score
print(f"Lowest Grade:          {lowest_score}")
print(f"Highest Grade:         {highest_score}")
print(f"Sum of Grades:         {sum_score}")
print(f"Average:               {ave_score:.2f}")
print("----------------------------------------")



