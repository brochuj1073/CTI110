# Justin Brochu
# 11/9/25
# P4HW2
# Time sheet of hours and pay

num_employee = 0
total_overtime = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

employ_name = input("Enter employee's name or \"Done\" to terminate: ")
while employ_name != "Done":
    
    hours_worked = float(input(f"How many hours did {employ_name} work? "))
    pay_rate = float(input(f"What is {employ_name}'s pay rate? "))
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        regular_hours = hours_worked
        overtime_pay = 0

    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    print(f"\nEmployee name: {employ_name}")
    print(f"\nHours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay      "  )
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.2f} {pay_rate:<12.2f} {overtime_hours:<12.2f} {overtime_pay:<15.2f} {total_regular_pay:<12.2f} {gross_pay:<12.2f}")

    

    num_employee += 1
    total_overtime += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    employ_name = input("\nEnter employee's name or \"Done\" to terminate: ")
    
print(f"\nTotal number of employees entered: {num_employee}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
print("-------------------------------------------------")