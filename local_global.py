#Local vs Global Variable

x = 10

print("Global variable:",x) # global variable

def myfunc():
    x = 20 #Local Variable
    print("Variable inside fucntion:",x)
    
myfunc()
print("Global variable:",x) # global variable

def globalfunc():
    global x
    x = 20 #Local Variable
    print("Variable inside function:",x)

globalfunc() 

print("Global variable after change in function",x) # global variable