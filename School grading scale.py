#Program to calculate the avg of the 5 sub marks. Display the corresponding grade.
p,q,r,s,t = int(input()),int(input()),int(input()),int(input()),int(input())
avg = (p+q+r+s+t)/5
if (avg>80):
    print("A")
elif (avg>=60 and avg<=80):
    print("B")
elif (avg>=50 and avg<60):
    print("C")
elif (avg>=45 and avg<50):
    print("D")
elif (avg>=25 and avg<45):
    print("E")
else :
    print("F")
