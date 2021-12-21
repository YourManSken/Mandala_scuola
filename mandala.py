import turtle
import random

turtle.speed(0)

def regular_polygon(side_number, side_length):
    if (side_number > 1 and side_number%1 == 0):
        if (side_length > 0):
            angle = 360/side_number
            turtle.left(angle/2)
            for _ in range(side_number):
                turtle.forward(side_length)
                turtle.right(angle)
            turtle.right(angle/2)
    #Return error checks
        else:
            print('Invalid side length')
    else:
        print('Invalid side number')

def regular_polygon_circle(polygon_number, polygon_color,  radius, side_number, side_length):
    if (polygon_number > 0 and polygon_number%1 == 0):
        if (radius > 0):
            angle = 360/polygon_number
            for _ in range(polygon_number):
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

def mandala(stages):
    for s in range(stages):
        polygon_number = random.randint(2, 60)
        polygon_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        radius = random.randrange(turtle.screensize()[1]*0.7/(stages-s))
        side_number = random.randint(3, 8)
        side_length = random.randint(10, 100)
        regular_polygon_circle(polygon_number, polygon_color,  radius, side_number, side_length)

mandala(2)
turtle.exitonclick()