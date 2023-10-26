with open('file.txt','r') as file:
    file.seek(15) #starting point of the character for reading
    characters = file.read(10)
    print(characters)
    print(file.mode)
    print(file.name)
    Type = type(characters)
    print(Type)