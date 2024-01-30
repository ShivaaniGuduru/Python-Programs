#Area Calculator: Write a program to calculate the area of a shape based on its type 
#(square, rectangle, circle, or triangle)
c = int(input("1.Square\n2.Rectangle\n3.Circle\n4.Triangle\n"))
if c==1:
    s = int(input("Enter the Side of a square :"))
    print(f'The area of the square is : {s*s}')
elif c==2:
    l,b = int(input("Enter the length of a rectangle :")),int(input("Enter the breadth of the rectangle :"))
    print(f'The area of the rectangle is : {l*b}')
elif c==3:
    r = int(input("Enter the radius of a circle :"))
    print(f'The area of a circle is :{22/7*r**2}')
elif c==4:
    w,h = int(input("Enter the width of a triangle :")),int(input("Enter the height of a triangle :"))
    print(f'The area of a triangle is :{0.5*w*h}')
else :
    print("Invalid Input")
