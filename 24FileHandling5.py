with open('file.txt','r') as file:
    file.seek(15) #starting point of the character for reading
    characters = file.read(10)
    print(characters)
    print(file.mode)
    print(file.name)
    Type = type(characters)
<<<<<<< HEAD
    print(Type)
    i = 0
    for line in file:
        print("Iteration", str(i), ": ", line)
        i = i + 1
    file.close()
    isclosed = file.closed
    print(isclosed)
=======
    print(Type)
>>>>>>> 09ac5f5ed46cb380388a90e324080ddfe21a1d83
