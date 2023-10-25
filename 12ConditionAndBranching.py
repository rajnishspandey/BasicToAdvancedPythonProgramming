#COMPARISION Operator
"""
equal: ==
not equal: !=
greater than: >
less than: <
greater than or equal to: >=
less than or equal to: <=
"""

#compare
a = 5
print("compare 1 :",a==8)

print("compare 2 :",'Testing' == 'Testing the Program')

print("compare 3 :",'A'>'B')
print("compare 4 :",'B'>'A')
print("compare 5 :",'AB'>'BA')
print("compare 6 :",'BA' > 'AB')

#greater than
i = 8
print("greater than :",i>6)

#inequality (not equals)
i = 2
print("inequality :",i!=6)
print("inequality :",i==2)


#BRANCHING

#IF statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


#ELSE statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Rainbow" )
    
print("move on")

# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Rainbow" )
    
print("move on")

## CONDITION statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')

# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

#LOGICAL OPERATOR
"""
and
or
not
"""

# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")






