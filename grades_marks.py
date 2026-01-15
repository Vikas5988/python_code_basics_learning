#To check the Grades according to Marks:

marks=int(input("Enter your marks : "))

if (marks<50):
    print("F Grade")
elif (marks>=81 and marks<100):
    print("A Grade")
elif (marks>=71 and marks<=80):
    print("B Grade")    
elif (marks>=61 and marks<=70):
    print("C Grade") 
elif (marks>=50 and marks<=60):
    print("D Grade")
else:
    print("Invalid Marks")
    