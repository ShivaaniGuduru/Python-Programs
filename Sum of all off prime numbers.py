#Program to print sum of all odd prime numbers
a,b = int(input()),int(input())
p = 0
for i in range(a,b+1):
    if (i%2==1):
        t = 0
        for j in range(1,i+1):
            if i%j==0:
                t = t+1
        if t==2:
            p = p+j
print(p)        
        
    
