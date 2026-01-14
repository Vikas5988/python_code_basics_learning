#Basic fucntion for beginners

# def addition(a=20,b=30):
# def addition(a,b):
#     sum=a+b
#     print("Sum of two given number",a, "and", b, "is :",sum)

# # addition(14,51)
# addition(a=45,b=7)
# # addition()

# def addition(a,b):
#      sum=a+b
#      #print("Sum of two given number",a, "and", b, "is :",sum)
#      return sum

# print("Addition of two number by function is : ",addition(11,51))

def addition(*num):
    print(type(num)) #List type
    sum=0
    for i in num:
        sum=sum + i
    return sum

#print("Addition of given number by function is : ",addition(11,51,8,5))
number=(11,22,33)
#print(type(number))
print("Addition of given number by function is : ",addition(*number))


