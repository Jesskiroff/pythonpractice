print("Welcome to the tip calculator! ")

total_bill =int(input ("What was the total bill? "))
tip_percentage= int(input ("How much tip would you like to give? 10%, 12%, or 15%?"))
number_of_people= int(input("How many people are splitting the bill? "))

price_per_person = (total_bill + ((total_bill * tip_percentage)/100))/number_of_people
print(F"Each person should pay {price_per_person} ")