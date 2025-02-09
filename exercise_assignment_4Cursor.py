# EA 4
# Robert Howe
# CIS156
# 1/30/25

# CHAPTER 6 (loops and loops within functions)

# 1. Write a while loop that adds the variable number to to the variable sum_of numbers.  Then it should prompt the user with text
# to enter another whole number (int) and add it to sum_of_numbers. The loop should iterate as long as the user
# enters an even whole number. The whole number can be positive or negative.
# Print sum_of_numbers AFTER EXITING the while loop (4 pts.).

sum_of_numbers = 0 # DO NOT DELETE THIS LINE OF CODE, USE THE VARIABLE IN THE WHILE LOOP
number = int(input('Enter a whole number: ')) # DO NOT DELETE OR MODIFY THIS LINE OF CODE
# The while loop should appear after this comment

while True:
        sum_of_numbers += number # The purpose of the program: add current number to the current sum
        next = input("Enter a whole number or hit the letter 'q' to get sum: ") # Invite user's input or "get sum"

        if next.lower() == 'q': # Check for user wants total via q key
                print(f"Here's your sum of digits: {sum_of_numbers}") # Quits summation loop, prints result
                #continue
                break

        number = int(next)  # Convert valid input to integer

""" Note to self: I need to review how to check for integers, the following throws an error:
if not next.lstrip('-').isdigit():  # Check if input is a whole number
                print("Invalid input. Please enter a whole number or 'q' to finish.")
"""

# 2. Write a for in loop to iterate over class_string, printing each letter on a separate line (2 pts.).
class_string = "PythonProgramming"  # DO NOT DELETE OR MODIFY THIS LINE OF CODE

# Per page 154, "for" loops: the variable (class_string) is incrementally assigned 1 character of the string.
for class_string in "PythonProgramming": # The "membership expression" is "class_string in "PythonProgramming"
    print(class_string)
# How about numbers and specials?
#for mixed_string in "CIS156Python!": # The "membership expression" is "mixed_string in "CIS156Python!"
#    print(mixed_string)
# yep, all characters

# 3. Write a for in loop that prints the numbers -4 through 10 on the same line with a comma after each number (3 pts.).
# Pg 155: use "range" to increment thru numbers, note the text "n=" is part of the reference formula
for n in range(-4,11): # Adding to the end of the range is a quick and dirty way to get the last digit.

    print(f"{n},", end=' ') # Added a "," as requested, and "end=' '" appparently bypasses LF/CR from the old days


# 4. Write a for in loop that prints the following set of numbers: 12 24 36 48 60 on one line with a space after each number
# by specifying the step value in the range. HINT: Research FOR loops and the parameters/arguments that can be accepted...
print() # DO NOT DELETE THIS LINE OF CODE
# Pg 155
for Ω in range(1,6): # Sets up the range of multiples of 12 to display; tried using \u03A9 for omega but not allowed.
    print(f"{Ω * 12} ", end=' ') # Formats the printout with a space and no linefeed; Ω as a copy/paste beats python limitations
 # Surprised at awkwardness of Python with greek characters in formulas: copy>paste? Really.
# 5. Write a nested FOR IN loop. Specifications:
# The outer loop's range should be between the numbers 1 through 5 inclusively using x as the variable. 
# The inner loop's range should be between the numbers -5 through -1 inclusively using y as the variable.
# Print the values of x and y inside the inner loop on the same line (3 pts.). 
print() # DO NOT DELETE THIS LINE OF CODE
# Page 157
for x in range(1,6): # Defines outer loop, numbers 1 thru 5 so there are 5 "x" passes, each with 5 "y" values attached
    for y in range(-5,0): # Defines the 5 "y" values coupled up with each of the 5 x's
        print(f"{x} {y}", end=' ') # Printout format; confusing at first, a ";" between "x" passes would clarify


# 6. Write a function that accepts two whole numbers as arguments
# First: to indicate a starting value
# Second: To indicate how many times the number will increase expoentially 
# The function will use the arguments to exponentially increase the starting number
# before the loop stops.
# The returned value should be printed to the console
# DO NOT USE a math built-in functions for this exercise
# (5 points)

print("This raises an integer Base number (B) to an integer power (P) without math functions")
B = int(input('Enter the base (B): '))  # User inputs the base number
P = int(input('Enter the power (P): '))  # User inputs the power number

result = 1  # Initialize result to 1 for multiplication
for _ in range(P):  # Setup loop P times multiplying B
    result *= B # The multiply

print(f"{B} to the power of {P} is: {result}")  # Print the result





