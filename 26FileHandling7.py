#'r' - read only
#'w' - write only
#'r+' -  Reading and writing. Cannot truncate the file.
#'w+' - Writing and reading. Truncates the file.
#'a+' : Appending and Reading. Creates a new file, if none exists. 
with open("file1.txt", 'w') as writefile:
    writefile.write("This is the line edited in main file\n")
    Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
    for writeline in Lines:
        writefile.write(writeline)
    
with open("file1.txt",'r') as readfile:
    readfile = readfile.read()
    print(readfile)

