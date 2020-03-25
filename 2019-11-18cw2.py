import random
import turtle
x = random.randint(1, 6)
def main(n):
    screen = turtle.Screen()
    kek = turtle.Turtle()
    kek.circle(n)
    kek.left(90)
    kek.up()
    kek.forward(n)
    kek.down()
    kek.circle(3)
    turtle.done()
main(99)
