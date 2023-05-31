#30773954 M Cindi#
#A Python script that will calculate the volume of a geometric shapes#
import math
Name=(input("Enter your name: "))
print("Hello," ,Name)
#Ask the user the to select a name of desired shape#
print("1. Helix")
print("2. Ellipse")
print("3. Exit")
Shape=float(input("Select a shape to calaculate its volume: "))
#Do if-statements#            
if   Shape==1:
     Raduis=float(input("Enter the radius in cm: "))
     Height=float(input("Enter the height in cm: "))
     HelixVolume=math.pi*Raduis**2*Height
     print("The volume of a Helix is: ",round(HelixVolume)," cubic cm")
elif Shape==2:
     a=float(input("Enter the length of a in cm: "))
     b=float(input("Enter the length of b in cm: "))
     c=float(input("Enter the length of c in cm: "))
     EllipseVolume=(4/3)*math.pi*a*b*c
     print("The volume of an Ellipse is: ",round(EllipseVolume),"cubic cm")
else :
     Shape==3
     exit()
