# Copy file to another

with open('file1.txt','r') as readfile:
    with open('file3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

# Verify if the copy is successfully executed

with open('file3.txt','r') as testwritefile:
    print(testwritefile.read())