#Program to read, write and manage files

# f=open("data.txt","rt")

# content= f.read()
# #content_new=f.read(3)
# print(f)
# print(content)
# #print("First 3 characters are: ",content_new)

f=open("data.txt","w")
f.write("Added text from code\n")
f.close()

f=open("data.txt","a")
f.write("Appended first line from code\n")
f.write("Appended second line from code\n")
f.write("Appended third line from code\n")
f.close()

#with open method, no need to close the file. it will automatically close the file
with open ("data.txt") as t:
   read_line=t.read()
print(read_line)    


 