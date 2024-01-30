#Write a Python program to input cost price and selling price of a product and check 
#profit or loss. Also calculate total profit or loss using if else and print it.
c,s = int(input()),int(input())
p = s-c
if (s>c):
    print("Profit:",p)
else :
    print("Loss:",p)
