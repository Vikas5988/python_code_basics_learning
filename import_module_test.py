#Learn Import module
import math
import math as m
from math import sqrt,pi

print("Available print function in Math module :",dir(math))

num1 = 16
num2 = 36
value1 = math.sqrt(num1)
value2 = m.sqrt(num2)  #Using m instead of math

value3 = sqrt(25)*pi
#print("Square root of ",num1," ",value1)

#print("Square root using AS keyword in import of ",num2," ",value2)

#print("Multiplication of square root of 25 and Pi is :",value3)
