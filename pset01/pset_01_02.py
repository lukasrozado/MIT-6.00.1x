#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'azcbobobegghakl'
count_bob = 0
for letters in range(len(s)):
    #NUMBERS OF LETTERS UNTIL FIND THE NUMBERS MATCHES WITH BOB NEEDS TO BE SLICED
    #BOB HAS 3 NUMBERS OF LETTERS 
    #SO ADDS LETTERS TO FIND THE EXATC MATCH OF LETTERS INSIDE THE STRING.
    if (s[letters:letters+3] == "bob"):
         count_bob += 1      
print("Number of vowels: " + str(count_bob))
