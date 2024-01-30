#Program to print all even numbers b/n 2001 to 3000 , which are factors of both 5&11
p,q = 2001,3000
for a in range(p,q+1):
    if a%2==0 and a%5==0 and a%11==0:
        print(a)
