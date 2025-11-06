# Justin Brohcu
# 10/26/25
# P3HW1
# Debug
# Correting code to debug

mod = []

mod.append(float(input("Enter grade for Module 1: ")))
mod.append(float(input("Enter grade for Module 2: ")))
mod.append(float(input("Enter grade for Module 3: ")))
mod.append(float(input("Enter grade for Module 4: ")))
mod.append(float(input("Enter grade for Module 5: ")))
mod.append(float(input("Enter grade for Module 6: ")))

# add grades entered to a list
print("\n------------Results------------")

# TO DO: determine lowest, highest , sum and average for grades

low = min(mod)
high = max(mod)
sum = sum(mod)
all_avg = len(mod)
avg = sum / all_avg

print(f"Lowest Grade:     {low}")
print(f"Highest Grade:    {high}")
print(f"Sum of Grades:    {sum}")
print(f"Average:         {avg: .2f}")

# determine letter grade for average

print("-------------------------------------")



if avg > 90:
   print(f"{avg} Your grade is: A")
else:
  if avg > 80:
    print(f"{avg} Your grade is: B")
  else:
    if avg > 70:
       print(f"{avg} Your grade is: C")
    else:
      if avg > 60:
         print(f"{avg} Your grade is: D")
      else: 
        if avg < 59:
           print(f"{avg} Your grade is: F")
  


   



