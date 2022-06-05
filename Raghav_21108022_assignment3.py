# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 23:39:09 2022

@author: Raghav
"""

#Made by- Raghav Jindal
#SID- 21108022
#Branch- Metallurgy

#Question 1

num=int(input("Enter the number you want to convert to binary"))
print("The binary equivalent of the number is",bin(num))



#Question 2

#My Calculator
first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")
if operator == "+":
 print(first + second)
elif operator == "-":
 print(first - second)
elif operator == "*":
 print(first * second)
elif operator == "/":
 print(first / second)
elif operator == "%":
 print(first % second)
else:
 print("Invalid Operation")



#Question 3

import math
print((3+4)*5)
n=int(input("Enter the number "))
exp2=n*(n-1)/2
print(exp2)
r=int(input("Enter the value of radius "))
exp3=4*3.14*r
print(exp3)
a=float(input("Enter the angle of cos"))
b=float(input("Enter the angle of sine"))
exp4=sqrt(r*math.cos(a)**2 + r*math.sin(b)**2)
print(exp4)
y1=float(input("Enter the 1st y coordinate "))
y2=float(input("Enter the 2nd y coordinate "))
x1=float(input("Enter the 1st x coordinate "))
x2=float(input("Enter the 2nd x coordinate "))
exp5=(y2-y1)/(x2-x1)
print(exp5)




#Question 4

n1=range(5)
for x in n1:
 print(x)
n2=range(3,10)
for x1 in n2:
 print(x1)
n3=range(4,13,3)
for x2 in n3:
 print(x2)
n4=range(13,5,-2)
for x3 in n4:
 print(x3)

n5=range(5,3)
for x4 in n5:
 print(x4)




#Question 5

numh=int(input("Enter the number of hydrogen :"))
numc=int(input("Enter the number of carbon :"))
numo=int(input("Enter the number of oxygen :"))

molecular_weight=1.00729*numh + 12.0107*numc + 15.9994*numo
print("The Molecular Weight of molecule is", molecular_weight )

























































