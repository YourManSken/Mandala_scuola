import turtle

def regular_polygon(side_number, side_length):
    if (side_number > 1 and side_number%1 == 0):
        if (side_length > 0):
            angle = 360/side_number
            turtle.left(angle/2)
            for l in range(side_number):
                turtle.forward(side_length)
                turtle.right(angle)
            turtle.right(angle/2)
    #Return error checks
        else:
            print('Invalid side length')
    else:
        print('Invalid side number')

def regular_polygon_circle(polygon_number, radius, side_number, side_length):
    if (polygon_number > 0 and polygon_number%1 == 0):
        if (radius > 0):
            angle = 360/polygon_number
            for p in range(polygon_number):
                turtle.penup()
                turtle.forward(radius)
                turtle.pendown()
                regular_polygon(side_number, side_length)
                turtle.penup()
                turtle.back(radius)
                turtle.right(angle)
        else:
            print('Invalid radius')
    else:
        print('Invalid polygon number')

#regular_polygon(4, 100)
regular_polygon_circle(20, 100, 4, 150)
input()