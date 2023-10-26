with open('file.txt','r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)


    if "Hello" in line1:
        print("This is the reading of first line")
    else:
        print("unable to read the first line of the file")