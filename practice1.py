#write a program to check input number is odd or even 

num = int(input("enter your number:"))

rem = num % 2

if(rem == 0):
    print("Even")

else:
    print("Odd")