#print("The Python interpreter converts written code to machine language")
#print("The IDE, integrated development environment I use is PyCharm, but it could be VScode.")
#print("inside of () with f says f-string, and anything inside {} aka placeholders, is an expression evaluated when run and can be a variable, computation, or other valid expression.")
x = 3
y = 7
#print(f"Example: sum of {x} and {y} equals {x + y}")
#name = Python
#print(f"{name.upper()} is awesome")
#To request input from the console, use input() which generates a prompt, the data is returned as a string.
#to get a visible prompt, provide a string: input("What is your name?: ")
# but the string is unassigned so goes nowhere, so assign a variable, "name"
#remember, if want to include variables, need to make it a f-string with f before the "
"""name = input("What is your name?: ")
age = input("How old are you?: ")
print(f"Hello, {name}")
print(f"Are you kidding, you're {age} years old?")
#if want to increment that age data, must convert it to integer via type
#typecasting; str, int, float, boolean
#use type(variable)
age = int(age)
#now increment
age += 1
print(f"In one year, you will be {age}. ")
# but better is to combine,
print("An alternative is to make the input integer to start:")
age = int(input("How old are you after this next birthday?"))
print("calculated by making the input an integer to start.")
print(f"In following year, you will be {age + 1}. ")
type(age)
#calcualte the area of rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is: {area}")
#to add dimensions, and a superscript 2, use alt 0178
print(F"The area is: {area} ft²")
print(type(area))"""

print("You will enter 3 words of at least 4 letters each when prompted, a portion of each will be combined to create a new 6 letter word.")
word1 = input("Enter your first word: ")
#if len(word1) >= 4:
word2 = input("Thanks, now enter your second word: ")
#else
#    print("Your first word must have at least 4 letters, try again.")
#if len(word2) >= 4:
word3 = input("Thanks, now enter your third word: ")
#else
#    print("Your second word must have at least 4 letters, try again.")
slice1 = word1[0:3]
slice2 = word2[0:2]
slice3 = word3[0:1]
combined = slice1 +slice2 + slice3
print(f"Great, here's your new custom word: {combined}")