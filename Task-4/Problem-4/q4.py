# Program to check if a number is palindrome or not
num=input(("Enter a num:"))
if(num==num[::-1]):
    print("The given number is a palindrome")
else:
    print("Not a palindrome")