#To explore readline function in File management

fr=open("data.txt","rt")
content= fr.read()
print("file read without readline funtion: \n",content)


f  = open("data.txt","r")
print("Read file with readline funtion")
while True:
    line_read=f.readline()   # Reads one line at a time
    if not line_read:        # If line is empty (EOF), break
        break
    print(line_read)