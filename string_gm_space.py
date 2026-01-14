# name=input("E.N.T.E.R--Y.O.U.R--N.A.M.E :")
# print("Good Morning",name)

single_space_name="Redhat Linux"
double_space_name="Redhat  Linux"

# print("find index of letter L:",single_space_name.find("L"))
# print("find index of letter L:",single_space_name.index("L"))

#Program to check double space in word

double_space_check1=single_space_name.find("  ")
print(double_space_check1)
double_space_check2=double_space_name.find("  ")
print(double_space_check2)

if double_space_check1 >= 0:
    print(single_space_name,"It contain double space")
else:
    print(single_space_name,"It does not contain double space")

if double_space_check2 >= 0:
    print(double_space_name,"It contain double space")
else:    
    print(double_space_name,"It does not contain double space")

print("Replace double space with hyphen :",double_space_name.replace("  ","-"))