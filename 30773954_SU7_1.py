#30773954 M Cindi#
#A Python script that prompts the user to enter their age and whether they have their ID card with them#
#Ask user details#
Age=float(input("Enter your age: " ))
Status=input("Enter your ID status('Y'/'N'): ")
#Checking if the user is able to buy alcohol#
if (Age>=18  and Status== "Y") :
     print("You are eligible to buy alcohol")
elif (Age<=18 and Status== "Y") :
     print("You are not eligible to buy alcohol")
else:
     print("Invaild Status")
