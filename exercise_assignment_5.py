# EA 5
# Robert Howe
# CIS156
# 2/8/2025

# CHAPTER 8

# 1. Assign any whole number to variable var_1 (1 pt.).
var_1 = 7
print("I assign a value of 7 to var_1")

# 2. Write an if statement that assigns 15 to the variable var_2 and -10 to the variable var_3
# and prints the sum of var_2 and var_3, if the variable var_1 is less than or equal to 15 (3 pts.).
if var_1 <= 15: # Given conditions
    var_2 = 15
    var_3 = -10
    print(f"Ans to Question#1: {var_2 + var_3}") # Based on var_1


# 3. Assign any whole number to var_4 (1 pt.).
var_4 = 23
print("I assign a value of 23 to var_4")
# 4. Write an if-else statement that prints out 'Yes, you definitely can', if var_4 is greater than 20 and
# prints out 'Nope.' if it is not greater than 20 (3 pts.).
if var_4 > 20: # Given condition
    print('Yes, you definitely can')
else:
    print('Nope.')


# 5. Assign any positive whole number to pulseRate (1 pt.).
pulseRate = 67

print("I assign s pulse rate of 67") # This question, like the others, would be more interesting if called for user input.
# 6. Write an if-else statement that prints 'Your pulse is normal' if pulseRate
# is within the range of 60 to 100, inclusively. If pulse is outside the range, print 'Your pulse rate may warrant further investigation by a medical professional' (4 pts.).
if 60 <= pulseRate <= 90: # Code  has clarity, simpler than I thought it could be, but probably not Pythonic.
    print(f"Your pulse {pulseRate} is normal")
else:
    print(f"Your pulse rate, {pulseRate} may warrant further investigation by a medical professional")


# 7. Use the try except keywords to verify that a user has entered a valid int value by
# prompting the user to enter an integer.  If the value is a valid integer, print out 'You entered a valid integer'.
# If the value is not a valid integer print out 'That is not a valid integer' (3 pts.).

try:
    user = int(input(f"Enter any integer: ")) # "try/except" is pretty slick, keep this in mind
    print("You entered a valid integer")
except ValueError:
    print("That is not a valid integer")
# I'd like to have it return to the input line; that's beyond the question but here it is:
while True:  # loop to keep asking for input if non-integer
    try:
        user = int(input("Enter any integer: "))
        print("You entered a valid integer")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("That is not a valid integer. Please try again.")



# 8. Import the random module and generate two random integer numbers. The first random number
# should be between -32 and -75 and the second random number should be between 32 and 92.
# Print both random numbers (4 pts.).
import random # Gets the random module
initiate8 = input("Hit enter to generate 2 random numbers. ") # I'm uneasy about just printing w/o explanation.
random_1 = random.randint(-75, -32) # Heartburn if range is backwards, the more negative no. has to be first
random_2 = random.randint(32, 92) # Remember the syntax, random_1.randint is no go, must be random.randint

print(f"(The first random number is: {random_1}, and the second one is : {random_2})")


# 9. Import the random module and generate five random integer numbers. 
# Each random number should be between 1 and 25
# Print all five random numbers PLUS the average value of the random numbers (5 pts.).
import random # random module
initiate9 = input("Hit enter to generate 5 random numbers and their average: ")
print("Here are your 5 random numbers:")
# Generate and print 5 unique random numbers between 1 and 25
random_1 = random.randint(1, 25)
print(random_1)
random_2 = random.randint(1, 25)
print(random_2)
random_3 = random.randint(1, 25)
print(random_3)
random_4 = random.randint(1, 25)
print(random_4)
random_5 = random.randint(1, 25)
print(random_5)
# Get and print the average
avg_5Random = (random_1 + random_2 + random_3 + random_4 + random_5) / 5
print(f"The average of these 5 random numbers is: {avg_5Random}")

