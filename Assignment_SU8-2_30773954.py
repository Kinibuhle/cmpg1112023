#30773954 M Cindi#
#A program that provide a sequence of numbers that will allow you to experiment with the for loop#
#Request info from the user#
Number=int(input("Enter any negative integer number: "))
#Output display#
print("Sequence of descending numbers from", 0 ," to number:",Number)
i=0
Addition=0
#Use a while loop, to display output in such a way that the number is printed, and all subsequent#
while (i>=Number): 
    print(i, end=" ")
    Addition=Addition+i
    i=i-1
print("\nSum: ",Addition)

exit()
