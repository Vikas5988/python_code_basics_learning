# Comparison: Without vs With Walrus Operator

# ----------- WITHOUT WALRUS -----------
print("---- Without Walrus ----")

num = 10                  # Step 1: assign value
if num > 5:               # Step 2: check condition
    print("Number is greater than 5")

print("Value of num is:", num)


# ----------- WITH WALRUS -----------
print("\n---- With Walrus ----")

if (num2 := 10) > 5:      # Assign + check in one line
    print("Number is greater than 5")

print("Value of num2 is:", num2)