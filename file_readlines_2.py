f=open("marks.txt","r")
i=0

# Start infinite loop to read file line by line
while True:
    i=i+1
    line=f.readline()
    
    # If line is empty (End Of File), stop the loop
    if not line:                  
        break
    
    # Split the line using comma as separator
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]       
    
    print(f"Marks of student {i} in Hindi : {m1}")
    print(f"Marks of student {i} in English : {m2}")
    print(f"Marks of student {i} in Math : {m3}")
    
    print(line)