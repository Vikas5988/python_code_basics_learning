#To write the data into a File

f=open("marks_new.txt","w")

marks=["English : 55\n", "Math:44\n", "Hindi: 65"]
f.writelines(marks)
f.close()
