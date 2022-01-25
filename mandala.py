import turtle
import random

#Init
turtle.speed(0)

#Crea un poligono regolare di side_number lati di lunghezza side_lenght
def regular_polygon(side_number, side_length):
    #Controlla possibili errori di input
    if (side_number > 1 and side_number%1 == 0):
        if (side_length > 0):
            #Codice effettivo
            angle = 360/side_number #Angolo di cui gira turtle
            turtle.left(angle/2)    #Raddrizza il poligono
            for _ in range(side_number):
                turtle.forward(side_length)
                turtle.right(angle)
            turtle.right(angle/2)   #Ritorna all'orientamento di partenza

    #Return error checks
        else:
            print('Invalid side length')
    else:
        print('Invalid side number')

#Crea un cerchio di raggio radius di polygon_number poligoni (vedi regular_polygon)
def regular_polygon_circle(polygon_number, radius, side_number, side_length):
    #Controlla possibili errori di input
    if (polygon_number > 0 and polygon_number%1 == 0):
        if (radius > 0):
            #Codice effettivo
            angle = 360/polygon_number  #Angolo al centro di cui gira turtle
            for _ in range(polygon_number):
                #Va al punto dove disegnare il poligono
                turtle.penup()
                turtle.forward(radius)
                turtle.pendown()
                #Disegna il poligono
                regular_polygon(side_number, side_length)
                #Torna indietro e gira
                turtle.penup()
                turtle.back(radius)
                turtle.right(angle)
    #Returns error checks
        else:
            print('Invalid radius')
    else:
        print('Invalid polygon number')

#Funzione che chiama regular_polygon_circle con parametri casuali stages volte
def mandala(stages):
    for s in range(stages):
        polygon_number = random.randint(2, 60)
        radius = random.randrange(turtle.screensize()[1]*0.7/(stages-s))
        side_number = random.randint(3, 8)
        side_length = random.randint(10, 100)
        regular_polygon_circle(polygon_number, radius, side_number, side_length)

#Crea un mandala casuale
mandala(2)

#Nasconde la turtle e non fa sparire subito il canvas
turtle.hideturtle()
turtle.exitonclick()