#given an intger , perform the following conditional actions:
#If n is odd,print Weird
#If n is even in the inclusive range of 2 to 5, print Not Weird
#If n is even in the inclusive range of 6 to 20, print Weird
#If n is even and greater  20, print Not Weird
n = int(input())
if (n%2!=0):
    print("Weird")
elif(n%2==0 and 1<=n<=5):
    print("Not Weird")
elif (n%2==0 and 6<=n<=20):
    print("Weird")
elif (n%2==0 and n>20):
    print("Not Weird")
