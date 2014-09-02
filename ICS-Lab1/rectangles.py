len1 = int(input("Enter length of rectangle 1 - "))
wid1 = int(input("Enter width of rectangle 1 - "))

len2 = int(input("Enter length of rectangle 2 - "))
wid2 = int(input("Enter length of rectangle 2 - "))


if ( len1 * wid1 ) > ( len2 * wid2 ):
    print("Rectangle 1 has the greater area!")
    
elif ( len1 * wid1 ) < ( len2 * wid2 ):
    print("Rectangle 2 has the greater area!")

else:
    print("The rectangles have equal areas!")
