#LIBRARIES
import re

#SEARCH 
#If apply, returns position of text

#Search For Specific Text
search=re.search(r"Random", "Random piece of text...")

print(search)
print("\n-----\n")

#Search Ignoring Lower and Upper Case
ignore=re.search(r"LOWER","We are ignoring if it has lower or upper case...", re.IGNORECASE)

print(ignore)
print("\n-----\n")

#Search Multiple Choice
multiple=re.search(r"[HJ]","lets try with Hello!")
multiple2=re.search(r"[0-9]","lets try with Hell0!")
multiple3=re.search(r"[A-Z]","lets try with Xello!")

print(multiple)
print(multiple2)
print(multiple3)
print("\n-----\n")

#FIND ALL
#If apply, returns all the instances that meet the conditions

findall=re.findall(r"[0-5]{4}", "1234 32312 11 35009 124")
print(findall)
print("\n-----\n")

#SUB
#If apply, substitutes selected text for prefixed string

sub=re.sub(r"Example", "[NAME]","My name is Example")
print(sub)
print("\n-----\n")

#SPLIT
#If apply, splits texts where the conditions meet

splt=re.split(r",","hello, this is, a random text...")
print(splt)
print("\n-----\n")



#KEYWORDS

#Letters 
pattern=r"[a-z]"       #a, Lower case
pattern=r"[A-Z]"       #A, Upper case
pattern=r"[\w]"        #Random, (Everything but spaces)

#Digits
pattern=r"[0-9]"       #3, Finds a digit
pattern=r"[\d]"        #312, Searches for group of digits

#Or
pattern=r"option A | option B"     #Will show any of the possible answers given by the parameter

#Negation
pattern=r"[^x]"        #0 (Anything but "x")

#Complete
pattern=r"Pro.*ing"    #Programming, Fills in between the two parameters

#Optional
pattern=r"p?each"      #each or peach, Works with both

#Reserved
pattern=r"\$100"       #Allows to print reserved chars, like ?*^

#Spaces
pattern=r"\s"          # Useful to find where a word ends

#Sum
pattern=r"o+k"         #Only looks for patterns were both chars are in a specific position

#Range
pattern=r"[a-z]{3}"    #hey (repeats a condition a number of times, in this case 3)
