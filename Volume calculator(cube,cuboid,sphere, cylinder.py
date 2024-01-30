#Volume Calculator: Write a program to calculate the volume of a shape based on its 
#type (cube, cuboid, sphere, or cylinder)
q = int(input("1.cube\n2.Cuboid\n3.Circle\n4.Cylinder\n"))
if q==1:
    s = int(input("Enter the side of the cube :"))
    print(f'The volume of a cube is :{s*s*s}')
elif q==2:
    l,b,h = int(input("Enter the length of cuboid :")),int(input("Enter the breadth of cuboid :")),int(input("Enter the height of cuboid :"))
    print(f'the volume of a cuboid is :{l*b*h}')
elif q==3:
    r = int(input("Enter the radius of sphere :"))
    print(f'The volume of a sphere is :{2*22/7*r}')
elif q==4:
    a,b = int(input("Enter the radius of cylinder :")),int(input("Enter the height of cylinder :"))
    print(f'The volume of a cylinder is :{22/7*a**2*b}')
else :
    print("Invalid Input")
    
