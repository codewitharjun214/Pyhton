#write a code for grade system using conditional statements 

marks = int(input("enter students marks :"))

if(marks >= 90):
   grade = "A"

elif(marks >= 80 and marks < 90):
    grade = "B"

elif(marks >= 70 and marks < 80):
    grade = "c"

else:
    grade = "D"

print("Grade of the student :" , grade)
