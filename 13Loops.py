#for loop - Use for loops when you know the number of iterations in advance and want to process each element in a sequence
"""
for val in sequence:
      # statement(s) to be executed in sequence as a part of the loop.
      """

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

#1
for color in colors:
    print(color)

#2 - range

for number in range(1,11):
    print(number) #starts with 1

print(range(3))

#2.1
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])

#OR

for i in dates:
    print(i)


#3
for number in range(11):
    print(number) #start with 0

#3.1
squares = ['red', 'yellow', 'green', 'purple', 'blue']
N = len(squares)
for i in range(N):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
    
#4
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i,squares in enumerate(squares):
    print(f"Index {i} is for square {squares}")

#4.1
for i, number in enumerate(range(1,11)):
    print(f"number {number} at the position {i}")

#4.2
# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for geners in Genres:
    print(geners)

#5
#While loop - Use while loops when you need to perform a task repeatedly as long as a certain condition holds true. 
"""
while condition:
    # Code to be executed while the condition is true
    # Indentation is crucial to indicate the scope of the loop
    """

count = 1
while count <=10:
    print(count)
    count=count+1
    #or
    #count += 1

#6
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]
while (year!=2000):
    print(year)
    i = i+1
    year = dates[i]

print("It took ", i ,"repetitions to get out of loop.")

#7
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while (i<len(squares) and squares[i]=='orange'):
    new_squares.append(squares[i])
    i = i+1
print(new_squares)

#8
# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while (i < len(PlayListRatings) and Rating >=6):
    print(Rating)
    i = i+1
    Rating = PlayListRatings[i]
    i = i+1