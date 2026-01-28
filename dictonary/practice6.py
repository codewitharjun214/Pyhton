#wap to enter marks of 3 students from the user and store them in a dictionary .start with an empty dictionary and add one by one . use subject name as a key and marks as a vakue 

marks = {}

x = int(input("enter phy :"))
marks.update({"phy" : x})

x = int(input("enter che :"))
marks.update({"che" : x})

x = int(input("enter bio :"))
marks.update({"bio" : x})

print(marks)