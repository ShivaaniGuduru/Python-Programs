#Program to check whether a year is leap year or not
y = int(input())
if (y%4==0)or(y%100!=0 and y%400==0):
    print(y,"is Leap Year")
else :
    print(y,"is not Leap Year")
