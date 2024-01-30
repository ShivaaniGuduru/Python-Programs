#Program to print all multiplication tables i.e from 1 to 20 tables
m,n = 1,20
for x in range(1,20+1):
    for y in range(1,11):
        print(f'{x}x{y}={x*y}')
    print(" ")
   
