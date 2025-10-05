# Justin Brochu
# 10/4/25
# Dictionary
# To store input from user and display output to the user

cars = {"Camaro" : 18.21, 
        "Prius" : 52.36,
        "Model S" : 110,
        "Silverado" : 26}

car_keys = cars.keys()
print(car_keys)

car_type = input("Enter a vehicle to see it's mpg: ")

car_mpg = cars[car_type]
print(f"The {car_type} gets {car_mpg} mpg.")

miles_drove = float(input(f"How many miles will you drive the {car_type}? "))

gallons_need = miles_drove/car_mpg

print(f"{gallons_need:.2f} gallon(s) of gas are needed to drive the {car_type} {miles_drove} miles." )




