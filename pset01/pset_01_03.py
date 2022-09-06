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