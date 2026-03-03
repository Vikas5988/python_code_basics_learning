with open ("data2.txt","r") as f:
    print(type(f))   
    read=f.read(6)      # Read the first 6 characters from the file
    print(read)
    
    f.seek(4)           # Move the file cursor to position 5 (6th character)
    
    print("Cursor current position : ",f.tell())     # Print the current cursor position (should output 5)
    read=f.read(6)      # Read the next 6 characters starting from position 5
    print(read)