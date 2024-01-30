#Program to print factorial and sum of n natural numbers
z = int(input())
c = 0
d = 1
for m in range(1,z+1):
    c = c+m
    d = d*m
print("Sum :",c)      
print("Factorial:",d)
    
