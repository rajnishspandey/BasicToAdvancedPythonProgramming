# Step 1: Open the file in read ('r') mode
file = open('file.txt','r')
# Step 2: Read the file content
readfile = file.read()
# Step 3: Process the content (e.g., print it)
print(readfile)
# Step 4: Close the file explicitly when done
file.close()

