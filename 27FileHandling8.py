#'r' - read only
#'w' - write only -- writes from first position and deletes all other existing data
#'a' - append -- appends the new data on the existing record
#'r+' -  Reading and writing. Cannot truncate the file.
#'w+' - Writing and reading. Truncates the file.
#'a+' : Appending and Reading. Creates a new file, if none exists.
#.tell() - returns the current position in bytes
#.seek(offset,from)
#readwritefile.truncate()
with open("file1.txt",'a+') as readwritefile: #try changing 'a+' with all other above commented characters
    readwritefile.write("Testing the append in the file let's see if it works or not\n")
    
    print(f"Initial Location: {readwritefile.tell()}")
    readfile = readwritefile.read()
    
    if (not readfile):
        print('file is empty')
    else:
        print("found the output \n",readfile)
    #uncomment below line
    #readwritefile.truncate()

    readwritefile.seek(0,0) # move 0 bytes from beginning.
    print(f"\nNew Location : {readwritefile.tell()}")
    data = readwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print(f"Location after read: {readwritefile.tell()}")
    