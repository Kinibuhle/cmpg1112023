#30773954 M Cindi#
#A Python script that prompts the user to enter two numbers and an operator (+, -, *, /) to perform a mathemaical operaion on those numbers#
#Asking the user to enter two numbers#
Number1=float(input("Enter the first number: "))
Number2=float(input("Enter the second number: "))
Operator=input("Enter the operator(+,-,*,/): ")
#Check for a division by zero error and print an error message if the user atempts to divide by zero#
if (Operator=='+'):
     Result=float(Number1+Number2)
     print("The result is: " ,Result)
elif (Operator== '-' ):
    Result=float(Number1-Number2)
    print("The result is: " ,Result)
elif (Operator== '*' ):
    Result=float(Number1*Number2)
    print("The result is: " ,Result) 
elif (Operator=='/' ):
    Result=float(Number1/Number2)
    print("The result is: " ,Result)
elif (Operator=='/' and Number2 or Number1==0):
  print("Error of division by zero" )
else:
    print("Error: Invalid Operator")
