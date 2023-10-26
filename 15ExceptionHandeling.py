"""
result = 10/0
print(result) #ZeroDivisionError


number = int('String')
print(number) # ValueError


with open("file.txt",'r') as file:
    content = file.read() #FileNotFoundError

mylist = [1,2,3,4,5,6,]
value = mylist[8]
print(value) #IndexError

text = "Example"
length = len(text)
missing  = text.some_method() #AttributeError
"""
#handling exception
try:
    result = 10/0
    print(result)

except ZeroDivisionError:
    print("error occured due to division by zero")

print("this is outside except block")

#################
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

###################
    a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)

#################
    a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
