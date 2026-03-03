with open("data_sample.txt","w") as f:
          f.write("1234567890")
          f.truncate(4)         # Truncate the file to only keep the first 4 bytes/characters ("1234")
          

# Open the same file in read mode to verify the content

with open("data_sample.txt","r") as f:         
    read=f.read()
    print(read)