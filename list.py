# # Creating a simple list of random fruits
# fruits = ["apple", "mango", "grape", "orange", "kiwi"]
# # Printing the list
# # Printing the list
# print(fruits)

#List of skill required for devops
devops_courses = ["Linux","AWS","Git","Terraform"]

print("List of skill for Devops career is ",devops_courses)

# print("Most important skill is : ", devops_courses[3])

devops_courses.append("Jenkins")
devops_courses.insert(3,"Docker")
devops_courses.insert(1,"Unix")
devops_courses.insert(4,"Github")

print("Updated list of required skill is :", devops_courses)

devops_courses.remove("Github")
devops_courses.pop(1)

print("new and correct list of required skill is :", devops_courses)







