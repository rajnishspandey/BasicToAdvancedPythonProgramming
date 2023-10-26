"""
To simplify file handling and ensure proper closure of files, Python provides the "with" statement. 
It automatically closes the file when operations within the indented block are completed. 
This is considered best practice when working with files.
"""

# Step 1: Open the file using 'with' in read ('r') mode
with open('file.txt','r') as file:
    # Step 2: Read the file content within the 'with' block
    content = file.read()
    # Step 3: Process the content (e.g., print it)
    print(content)

# Step 4: The file is automatically closed when the 'with' block exits