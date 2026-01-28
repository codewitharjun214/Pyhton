#print the elements of list using for loop 

nums = [ 1,4,6,7,9,45,34,45,533,9]
x = 9
idx = 0
for el in nums:
    if(el==x):
        print("number found at idx",idx)
        break
 idx +=1
    

