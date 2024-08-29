# Your Life in Weeks
# Instructions
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

#     You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input

# 56

# Example Output

# You have 12410 days, 1768 weeks, and 408 months left.

# Hint

#     There are 365 days in a year, 52 weeks in a year and 12 months in a year.
#     Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

anhos_restantes = 90 - int(age)

months_restantes = anhos_restantes * 12

weeks_restantes = anhos_restantes * 52

days_restantes = anhos_restantes * 365

print(f"You have {days_restantes} days, {weeks_restantes} weeks, and {months_restantes} months left")



