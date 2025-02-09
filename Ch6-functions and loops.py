#num_letters = len("seven")
#print(num_letters)
#returnval = print("wazzupt")
#print(returnval)
#def enrolled(enrolled):
#    print(f"{enrolled}")
#enrolled = (I was enrolled in CIS156 during Spring 2025)
# EA 3
# Robert Howe
# 1/29/25
# CIS156 27552
"""
# #1 Write a function that prints the line of text & returns no value
def enrolled(CIS156_enrollment): # Define the function, signature
    print(CIS156_enrollment) # To print it, within function
# I'm a bit murky on separating #1 and #2, as the rubric requires printing in #1 and #2
(CIS156_enrollment) = "I was enrolled in CIS156 during Spring 2025" # Function body
print("Answer #1")
#print(CIS156_enrollment) # If I didn't need to test for no value
result = enrolled(CIS156_enrollment) # Calls and tests
print(f"What value is returned? {result}") # Confirms no value

#2 Call & confirm
print("Answer #2")
enrolled(CIS156_enrollment) # Call the function
#print(f"Call again and test, What value is returned? {result}")# Test for no value
#result = enrolled(CIS156_enrollment) # Calls, duplicates text, tests for no value


#3 write New function, 1 argument, setup to print, no value
print ("Answer #3")
def greeting(name): # New function
    print(f"Hello, {name} it is great to meet you!") # Setup to print
print(f"Testing function 'greeting', what value is returned? {result}") # Confirms no value;

#4 Now print with argument of Bulbasaur
print ("Answer #4")
result = greeting("Bulbasaur")
print(f"The value returned is: {result}")

#5 Create function four_args, parameters a,b,c,d and values 15.5, 8.3, -10, and 30, answer w/b "returned_value"
print("Answer #5")

Assignment4
# 1. Write a while loop that adds the variable number to to the variable sum_of numbers.  Then it should prompt the user with text
# to enter another whole number (int) and add it to sum_of_numbers. The loop should iterate as long as the user
# enters an even whole number. The whole number can be positive or negative.
# Print sum_of_numbers AFTER EXITING the while loop (4 pts.).

sum_of_numbers = 0  # DO NOT DELETE THIS LINE OF CODE, USE THE VARIABLE IN THE WHILE LOOP
number = int(input('Enter a whole number: '))  # DO NOT DELETE OR MODIFY THIS LINE OF CODE
# The while loop should appear after this comment

while True:
    sum_of_numbers += number  # The purpose of the program: sum whole numbers
    next = input("Enter another whole number or hit the letter 'q' to finish: ")  # Invite user's input
    # Check for user desires the total via q key
    if next.lower() == 'q':
        print(f"Here's your sum of digits: {sum_of_numbers}")  # Quits summation loop, prints result
        # continue
        break
# Note: I need to review how to check for integers, the following throws an error:
if not next.lstrip('-').isdigit():  # Check if input is a whole number
                print("Invalid input. Please enter a whole number or 'q' to finish.")
                #continue
"""
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
print()  # DO NOT DELETE THIS LINE OF CODE
# Pg 155
for Ω in range(1,6): # Sets up the range of multiples of 12 to display; tried using \u03A9 for omega but not allowed.
    print(f"{Ω * 12} ", end=' ') # Formats the printout with a space and no linefeed; Ω as a copy/paste beats python limitations

# 5. Write a nested FOR IN loop. Specifications:
# The outer loop's range should be between the numbers 1 through 5 inclusively using x as the variable.
# The inner loop's range should be between the numbers -5 through -1 inclusively using y as the variable.
# Print the values of x and y inside the inner loop on the same line (3 pts.).
print()  # DO NOT DELETE THIS LINE OF CODE
# Page 157
for x in range(1,6): # Defines outer loop, numbers 1 thru 5 so there are 5 "x" passes, each with 5 "y" values attached
    for y in range(-5,0): # Defines the 5 "y" values coupled up with each of the 5 x's
        print(f"{x} {y}", end=' ') # Printout format; confusing at first, a ";" between "x" passes would clarify

"""

# 6. Write a function that accepts two whole numbers as arguments
# First: to indicate a starting value
# Second: To indicate how many times the number will increase expoentially
# The function will use the arguments to exponentially increase the starting number
# before the loop stops.
# The returned value should be printed to the console
# DO NOT USE a math built-in functions for this exercise
# (5 points)
"""print() # Does a LF-CR from prior printout.
print("This raises an integer Base number (B) to integer power (P) without math functions")
B = 0
P = 0
B2P = 1
B = int(input("Enter the base number, B:")) # Fix console input, string to integer.
P = int(input("Enter the power, P:"))
#for i in range(0, P+1): # Iterates from 0 to Pth power by multiplying w/o exp or ** function
for _ in range(P):
    B2P *= B  # Multiply B by itself P times

print(f"B2P, {B} raised to the {P}th power is: {B2P}")


print("This raises an integer Base number (B) to an integer power (P) without math functions")
B = int(input('Enter the base (B): '))  # User inputs the base number
P = int(input('Enter the power (P): '))  # User inputs the power number

result = 1  # Initialize result to 1 for multiplication
for _ in range(P):  # Loop P times multiplying B
    result *= B

print(f"{B} to the power of {P} is: {result}")  # Print the result
"""
