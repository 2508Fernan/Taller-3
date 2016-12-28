from turtle import*
import time
import turtle
t= turtle.Pen()
##tamaño de la ventana
turtle.setup (500,600)
##establecer el objeto en pantalla
wn= turtle.Screen()
##color de la pantalla
wn.bgcolor("pink")
##titulo de la pantalla
wn.title("Estrella de Puntas Pares")
a=int(input("ingrese un numero par:"))
print(a)
for x in range (1,21):
    t.pencolor("sky blue")
    t.pensize(4)
    t.forward(100)
    an=180/a
    ang=180 - an
    t.left(ang)
turtle.getscreen()._root.mainloop()

