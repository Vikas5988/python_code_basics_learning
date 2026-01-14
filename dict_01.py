#Dictionary 

Devops_tool_mapping={"OS":"Linux","Cloud":"AWS","CI/CD Tools":["Jenkins","Github Action"]}

print("List of Devops skill with required tools:", Devops_tool_mapping)

print("First method to fetch the value, OS to learn for Devops:", Devops_tool_mapping["OS"])

print ("Second method to fetch the value, Cloud to Learn :", Devops_tool_mapping.get("OS"))

print(Devops_tool_mapping.items()) #To print the dictionary

#To Print keys in dictionary not values
print(Devops_tool_mapping.keys()) 

#To update the key value in Dictionary
(Devops_tool_mapping.update({"Iac":"Terraform/Cloudformation"}))
print("List of updated tools:", Devops_tool_mapping)
