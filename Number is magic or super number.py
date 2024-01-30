#Program to print given number is magic or super number
#Let’s take input number is 5 .Then
#1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283333333333333, let’s say this result as x And 1/2 + 2/3 + 3/4 + 4/5 + 5/6 = 3.5500000000000003, let’s say this result as y
#Then multiply both and cast it to int i.`e. int(x*y), let’s say this result as z
#Now if z is even number then it is Magic Number else it is super number After above operations we will get result as 8 as it is even number output should be Magic Number
s = int(input())
h,i = 0,0
for v in range(1,s+1):
    h = h+(1/v)
    i = i+(v/(v+1))
a = int(h*i)
if a%2==0:
    print("Magical Number")
else :
    print("Super Number")
    
