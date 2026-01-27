#write a program to find the gretest of 3 numbers entered by the user 

a = int(input("enter your number :"))
b = int(input("enter your number :"))
c = int(input("enter your number :"))

if(a>b and a>c):
    print("first number is largest",a)

elif(b >= c):
    print("second number is largest" ,b)

else:
    print("third is largest : ", c)