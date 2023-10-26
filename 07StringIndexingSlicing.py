#Strin's Indexing and Slicing

#String
name = "Michael Jordan"
print(name)
print(type(name))

#indexing

print(name[0])
print(name[6])

#negative indexing
print(name[-1])
print(name[-5])

#length
print("lenght of string:",len(name)) #len is onyl applicable for Strings not for int or float


#slicing

print(name[0:4])
print(name[:4])
print(name[:4:2]) #here 2 means every 2nd value

#concatinating

print("Hello "+name)

#escape chars

print("Hello \n"+name)
print("Hello \t"+name)
print("Hello \\ "+name)

#string Operations
print("upper case :",name.upper()) #upper()
print("lower case :",name.lower()) #lower()
print("replace :",name.replace("Michael","Testing")) #replace()
print("find :",name.find("J")) #find()
print(name.find("Jasdfasdasdf"))
print("Split :",name.split()) #split()
##################################################################
print('################################################')
#Regular expression

import re #importing regex

string =  "Michael Jordan is the best"
pattern = "Michael"
result = re.search(pattern,string)
print(result)
if result:
    print("match Found")
else:
    print("match not found")

################################################
print('################################################')
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits

text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

############################################
print('################################################')
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

#############################################
print('################################################')
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)


#############################################
print('################################################')
# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)


#############################################
print('################################################')
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string)