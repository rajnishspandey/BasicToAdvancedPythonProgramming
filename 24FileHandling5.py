with open('file.txt','r') as file:
    file.seek(15) #starting point of the character for reading
    characters = file.read(10)
    print(characters)
    print(file.mode)
    print(file.name)
    Type = type(characters)
    print(Type)
    i = 0
    for line in file:
        print("Iteration", str(i), ": ", line)
        i = i + 1
    file.close()
    isclosed = file.closed
    print(isclosed)
