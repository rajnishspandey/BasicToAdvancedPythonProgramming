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
