import turtle
import datetime
tut = turtle.Turtle()
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
print(hour, minute, second)
class face():
    def draw_clock(self):
        tut.penup()
        tut.goto(0, -250)
        tut.color('cyan')
        tut.down()
        tut.circle(250)
        tut.penup()
        tut.color('blue')
        tut.goto(0, 0)
        tut.setheading(90)
        tut.right(hour*360/12)
        tut.pendown()

