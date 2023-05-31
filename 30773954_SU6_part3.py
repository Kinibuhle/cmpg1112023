#30773954 Cindi M#
#Ask the user to provide a character as input,then display the ASCII value of that character.#
print("**ASCII and character conversion**")
char=input("Enter a character: ")
#display the ASCII value of that character#
ASCIIValue=ord(char)
print("The ASCII value is : " , ASCIIValue )
#Ask the user to provide an ASCII value (int)#
ASCIIValueInt=int(input("Enter a ASCII value: "))
#display the character#
Character=chr(ASCIIValueInt)
print("The character is : ",Character)
