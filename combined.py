# Robert Howe
# PA 2
# CIS156 Fall 2025 slicing


# Assignment is slicing only, tests of the input for alpha's (isalpha()) or 4 characters minimum (len())
# Without these tests, bogus inputs get processed as follows:
# 3 "words" like 1234 yield a combined of 123341; "shorter words" a, up, er yields aupe.
# After a bit of struggle, I included the 3 test loops.   Why the course text has no topic index is a mystery

print("When prompted, please enter 3 words of at least 4 letters each.")
print("Then a portion of each will be combined to create a new 6 letter word.")
bogus = 0
while True:  # testing added, stumbles noted.
    word1 = input("Enter your first word: ")
    if len(word1) < 4 or not word1.isalpha(): # OK, the : goes at the end, nothing in the ()
        print("Your first word must have at least 4 letters, no blanks or numbers. Try again.") # if bogus input
        bogus += 1
        continue # and the continue needs the indent
    break # and the break gets outdent.
while True:
    word2 = input("Thanks, now enter your second word: ")
    if len(word2) < 4 or not word2.isalpha():
        print("Your second word must have at least 4 letters, no blanks or numbers. Try again.")
        bogus += 1
        continue
    break
while True:
    word3 = input("Thanks, now enter your third word: ")
    if len(word3) < 4 or not word3.isalpha():
        print("Your third word must have at least 4 letters, no blanks or numbers. Try again.")
        bogus += 1
        continue
    break
slice1 = word1[0:3]
slice2 = word2[-2:] # mis-read the instructions, lucky catch, always use the example
slice3 = word3[0:1]
combined = slice1 +slice2 + slice3
print(f"Congratulations, your new custom word is: {combined}")
print(f"There were {bogus} rejected inputs.") # Added at last minute, I like it.
# Checks out; "First, second, third" yields "Firndt". blanks, short count, and non-alpha blocked.