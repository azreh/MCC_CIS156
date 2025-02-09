# EA 3
# Robert Howe
# 1/29//25
# CIS156 27552

# CHAPTER 6 

# 1. Write a function called enrolled that just prints the following: 
#    I was enrolled in CIS156 during Spring 2025.
#    No arguments should be passed into the function, and the function should not return a value. (2 pts.)
def enrolled(CIS156_enrollment): # Define the function, signature
    print(CIS156_enrollment) # To print it, within function
""" I'm a bit murky on separating #1 and #2, as the rubric seems to require printing in both #1 and #2"""
(CIS156_enrollment) = "I was enrolled in CIS156 during Spring 2025" # Function body
#print("Answer #1")
#print(CIS156_enrollment) # If I didn't need to test for no value; # to prevent double printint
result = enrolled(CIS156_enrollment) # Calls and tests
print(f"What value is returned? {result}") # Confirms no value

# 2. Write a statement to call the enrolled function. (1 pt.)
enrolled(CIS156_enrollment) # Call the function
#print(f"Call again and test, What value is returned? {result}")# Test for no value
#result = enrolled(CIS156_enrollment) # Calls, duplicates text, tests for no value


# 3. Write a function named greeting. The function should accept ONE argument, the
#    name of the person you are greeting and PRINT the following: 
#    Hello <name argument>, it is great to meet you!
#    The function should not return a value. (2 pts.)
def greeting(name): # New function
    print(f"Hello, {name} it is great to meet you!") # Setup to print
print(f"Testing function 'greeting', what value is returned? {result}") # Confirms no value;

# 4. Write a statement to call the greeting function passing in an argument of Bulbasaur. (1 pt.)
#print ("Answer #4")
result = greeting("Bulbasaur")
print(f"The value returned is: {result}")

# 5. Write a statement to call the four_args function passing in a value of 15.5 that will be assigned to parameter a,
#    a value of 8.3 that will be assigned to parameter b, a value of -10 that will be assigned to parameter c,
#    and a value of 30 that will be assigned to parameter d. 
#    Save the returned answer in a variable named returned_value. Print returned_value. (4 pts.)
def four_args(a, b, c, d):   # DO NOT DELETE OR UPDATE THIS FUNCTION
    answer = a + b * c + d   # DO NOT DELETE OR UPDATE THIS FUNCTION
    return answer            # DO NOT DELETE OR UPDATE THIS FUNCTION
def four_args(a,b,c,d):
    answer = a + b * c + d
    return answer


four_args(15.5,8.3,-10,30)
print(f"Answer #5: {four_args(15.5,8.3,-10,30)}")
result = four_args(15.5,8.3,-10,30)
print(f" The value returned is: {result}")
# Should I clean up comments from scratchpad/sandbox/whatever, before cut and paste to assignment sheet?
