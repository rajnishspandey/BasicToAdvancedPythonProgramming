with open('file.txt','r') as file:
    while True:
        line = file.readline()
        if not line:
            break #stop when lines are not found
        print(line)