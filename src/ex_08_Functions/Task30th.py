#Q - Create a function which will take the 3 values from the user, which are length of the triangle.
# side1, side2, side2

def triangle(side1, side2, side3):
    if side1 == side2 == side3:
        print("Triangle is Equilateral")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Triangle is Isosceles")
    else:
        print("Triangle is Scalene")

triangle(5, 5, 5)   # Triangle is Equilateral
triangle(5, 5, 3)   # Triangle is Isosceles
triangle(3, 4, 5)   # Triangle is Scalene