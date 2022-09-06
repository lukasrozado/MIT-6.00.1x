# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your
# program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If 
# you've spent more than a few hours on this problem, we suggest that you move 
# on to a different part of the course. If you have time, come back to this 
# problem after you've had a break and cleared your head.


my_string = "azcbobobegghakl"
current_string = ""
longest_string = ""
for letters in range(len(my_string)):
    #IF MY ACTUAL STRING LETTER IS GREATER THAN MY PREVIOUS STRING LETTER
    if (my_string[letters] >= my_string[letters-1]):
        # THEN ADD TO THE CURRENT STRING AND CONCATENETE.
        current_string += my_string[letters]
        # IF NOT GREATER THAN KEEP THE SAME.
    else:
        current_string = my_string[letters]
    #THEN COMPARE THE CURRENT STRING WITH THE LONGEST STRING AND UPDATE THE VALUE.
    if len(current_string) > len(longest_string):
        longest_string = current_string
print(longest_string)