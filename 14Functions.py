def calculate_total(a,b):
    c = a+b
    return c

result = calculate_total(2,3)
print("calculate_total : ",result)

#len
string_length = len("Hello, World!")
print(string_length)
list_length = len([1, 2, 3, 4, 5])
print(list_length)

#sum

total = sum([10, 20, 30, 40, 50])
print(total)

#max
highest = max([10, 20, 30, 40, 50])
print(highest)

lowest = min([10, 20, 30, 40, 50])
print(lowest)


#pass
def test():
    pass

print(test())


def greet(name):
    print("Hello, " + name)
    
result = greet("Alice")
print(result)  # Output: Hello, Alice, None (it is returning none because we are not using Return in the function - function always has return value if nothing is returned then by default it returns None)

for _ in range(3):
    print(greet("Alice"))


#docstring
def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)


#scope of variable
global_variable = "I'm global"
def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

print(example_function())

print(global_variable)

#function with loop
def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)
print_numbers(5)  # Output: 1 2 3 4 5

# Define an empty list as the initial data structure
my_list = []
print(my_list)
data_structure = [1,2,3,4,4]

# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)

print(data_structure)

# Function to remove an element from the list
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

print(remove_element(data_structure,1))
print(data_structure)


L=[1,3,2]
print(sorted(L))

def Print(A):
    for a in A:
        print(a+'1')
        print(['a','b','c'])

Print('A')


#####################
def add(a):
    """
    add 1 to 0
    """
    b = a+1
    return b

help(add)

####################


def square(a):
    b = a*a
    return b

print(square(2))

###############
def test():
    print("test")

test()
print(test())


###################
#When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


def Testing(*args):
    for i in args:
        print(i)

Testing(1,2,3,4,5,6,7,)
######################
#Similarly, The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')


def student(**args):
    for key in args:
        print(key + " : "+args[key])

student(TestName1 = 'Alice', TestName2 = 'John')

##########################
def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print(myList)