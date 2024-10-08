#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Tip Calculator
# Instructions

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Example Input

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Example Output

# Each person should pay: $19.93

# Hint

#     How to round a number to 2 decimal places in Python
#     How to limit a float to two decimal places in Python

#Mi respuesta

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
porcentaje_propina = tip/100
propina = bill * porcentaje_propina
total_bill = bill + propina
bill_por_persona = total_bill/people
bill_round = round(bill_por_persona, 2)
bill_round = "{:.2f}".format(bill_por_persona)
print(f"Each person should pay: ${bill_round}")

#Respuesta de la profesora 

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
# people = int(input("How many people to split the bill?"))
# tip_as_percent = tip/100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill/people
# final_amount = round(bill_per_person,2)
# print(f"Each person should pay: ${final_amount}")
