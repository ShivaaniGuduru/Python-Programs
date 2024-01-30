#Program to print maximum of three numbers
i,j,k = int(input()),int(input()),int(input())
if (i>j and i>k):
    print(i)
elif (j>k):
    print(j)
else :
    print(k)
