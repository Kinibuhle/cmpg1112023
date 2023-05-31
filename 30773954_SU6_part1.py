#30773954 CINDI M#

#A program that can determine the area, volume and diagonal of a cone#
import math
print("Cone Calculator")
Raduis=float(input("Enter the radius in cm: "))
Height=float(input("Enter the height in cm: "))           
#Calculations of the cone using given formulas#
Area= math.pi* Raduis* (Raduis + math.sqrt(Height**2+Raduis**2))
Diagonal=(math.sqrt(Raduis**2 +Height**2))
Volume=(math.pi*Raduis**2*Height)/3
#Displaying the results#
print("Area of a cone is "  ,round(Area,4) , " square cm")
print("Space diagonal of the cone is " , round(Diagonal,3) ," cm")
print("Volume of a cone is ",  round(Volume,2) , " cm")
print("**Cone Dimensions**")
print("Raduis= " ,round(Raduis,1),  "Height= ",round(Height,1))
