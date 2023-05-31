#30773954 Cindi M#
#program that calculates the two roots of a quadratic equation#
import math
#Ask the user to supply the coefficients (a, b, and c) #
print("Solving ax^2+bx+c =0")
A=float(input("Enter the coeffiecient of a: "))
B=float(input("Enter the coefficient of b: "))
C=float(input("Enter the coefficient of c: "))
#calculate x1 and x2 using the formulas#
X1=(-B +math.sqrt(B**2-4*A*C))/(2*A)
X2=(-B -math.sqrt(B**2-4*A*C))/(2*A)
#Displaying the roots#
print("ROOTS OF GIVEN QUADRATIC EQUATIONS ARE: ")
print("X1: ",round (X1,1))
print("X2: ",round (X2,1))
               
