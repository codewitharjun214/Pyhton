#1234 check it plindrome or not


num = 1234
originsl = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if originsl == rev:
    print("The number is palindrome")   
else:
    print("The number is not palindrome")
