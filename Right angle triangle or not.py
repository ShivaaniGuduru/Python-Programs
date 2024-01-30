#Take three sides of a triangle as input from the keyboard and print weather it is right 
#angled triangle or not, where take 3 angles of the triangle as input from the keyboard


s1,s2,s3 = int(input("Enter s1 :")),int(input("Enter s2 :")),int(input("Enter s3 :"))
if ((s1**2+s2**2==s3**2) or (s2**2+s3**2==s1**2) or (s3**2+s1**2==s2**2)):
    print("The triangle is right angle triangle")
else :
    print("The triangle is not a right angle triangle")
