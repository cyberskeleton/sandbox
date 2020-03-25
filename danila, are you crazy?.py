import turtle
import time
import random

delay = 0.2

window = turtle.Screen()
window.title('snek game by epic gamer')
window.bgcolor('cyan')
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('purple')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(0, 100)

segments = []
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('score: 0  high score: 0', align='center', font=('Times New Roman', 24, 'normal'))



def goup():
    if head.direction != 'down':
        head.direction = 'up'


def godown():
    if head.direction != 'up':
        head.direction = 'down'


def goleft():
    if head.direction != 'right':
        head.direction = 'left'


def goright():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

window.listen()
window.onkeypress(goup, 'w')
window.onkeypress(godown, 's')
window.onkeypress(goleft, 'a')
window.onkeypress(goright, 'd')
while True:
    window.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.2
        pen.clear()
        pen.write('score: {} high score: {}'.format(score, high_score), align='center', font=('Times New Roman', 24, 'normal'))
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape('square')
        newsegment.color('pink')
        newsegment.penup()
        segments.append(newsegment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('score: {} high score: {}'.format(score, high_score), align='center', font=('Times New Roman', 24, 'normal'))
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.2
            pen.clear()
            pen.write('score: {} high score: {}'.format(score, high_score), align='center', font=('Times New Roman', 24, 'normal'))
    time.sleep(delay)

#window.mainloop()
