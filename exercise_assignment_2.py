# EA 2
# Last updated Fall 2023
# Robert Howe

# CHAPTER 5

# 1. Create a variable named num_1 and assign 28 to it (1 pt.).
num_1 = 28

# 2. Create a variable named num_2 and assign 63 to it (1 pt.).
num_2 = 63

# 3. Add num_1 to num_2 and store it in ans_one, print ans_one (2 pts.).
ans_one = (num_1 + num_2)
print(ans_one)
#I like the alternative narrative version to reinforce memorization
print(f"The sum of {num_1} and {num_2} is: {ans_one}")

# 4. Subtract num_1 from num_2 and store it in ans_two, print ans_two (2 pts.).
ans_two = (num_2 - num_1)
print(f"{num_2} subtracted from {num_1} is: {ans_two}")

# 5. Multiply num_1 by num_2 and store it in ans_three, print ans_three (2 pts.).
ans_three = (num_1 * num_2)
print(f"The product of {num_1} times {num_2} is: {ans_three}")

# 6. Divide num_2 by num_1 and store it in ans_four, print ans_four (2 pts.).
ans_four = (num_2 / num_1)
print(f"{num_2} divided by {num_1} equals: {ans_four}")

# 7. Use the integer division operator to divide num_2 by num_1 and store it in ans_five, print ans_five (2 pts.).
ans_five = (num_2 // num_1)
print(f"The result of integer division of {num_2} divided by {num_1} is: {ans_five}")

# 8. Return the remainder of num_2 divided by num_1 and store it in ans_six, print ans_six (2 pts.).
#By specifying the remainder, an integer division is implied, but float would be instructive to see
#ans_six via integer
ans_six = (num_2 % num_1)
print (f"The remainder (modulus) of integer division of {num_2} by {num_1} is: {ans_six}")
#Note the difference between ans_4's fractional portion(0.25) and ans_8 (7) which is get_fractional_part{ans_4} * num_1
#another way is
# #ans_sixa = ans_four % 1
#print(f"extracting the fractional portion yields: {ans_sixa}")

#9. Use the is_integer method to check if num is an integer and print the value returned by the method (2 pts.).
num = 28.6 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
print(f"Test result, is {num} an integer? {num.is_integer()}")

# 10. Use the pow function to print out 6 raised to the power of -4 (1 pt.).
print(f"six to the -4 power using ** is: {6 ** -4}, and using pow() is {pow(6, -4)} but if you mistakenly use 6e-4 you'll get {6e-4}")

# 11. Print num_3 so that 3 decimal places are displayed and it is grouped by thousands (1 pt.).
num_3 = 987654321.123456789 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
#print(f"Num_3 formatted and rounded is {num_3: , .3f}") very fussy about spaces!
print(f"Num_3 formatted and rounded is {num_3:,.3f}")

# 12. Write a print statement using an f-string that prints out the following sentence using the variables defined below.
# In 2020, Australia had a population of 25,660,000 and a life expectancy of 83.2 years. The round function
# should not be used (2 pts.).
year = 2020 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
population = 25660000 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
expectancy = 83.2031 # DO NOT DELETE OR MODIFY THIS LINE OF CODE

print(f"In {year} Australia had a population of {population:,} and a life expectancy of {expectancy:.1f} years")


