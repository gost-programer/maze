from turtle import *
import time
import random

score = 0

# Window
win = Screen()
win.title('Snake Game')
win.bgcolor('green')
win.setup(width=600, height=600)
win.tracer(0)

# Snake
snake = Turtle()
snake.speed(0)
snake.shape('square')
snake.color('white')
snake.penup()
snake.direction = 'stop'

# food
food = Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

# segments
segments = []

# functions
def goup():
    snake.direction = 'up'

def godown():
    snake.direction = 'down'

def goright():
    snake.direction = 'right'

def goleft():
    snake.direction = 'left'

def move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

win.listen()
win.onkeypress(goup,'w')
win.onkeypress(godown,'s')
win.onkeypress(goleft, 'a')
win.onkeypress(goright, 'd')


while True:
    win.update()

    # Wall
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        print('Game over')
        snake.goto(0,0)
        snake.direction = 'stop'

        # hid segments
        for s in segments:
            s.goto(1000,1000)

        segments.clear()
        score = 0
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)



    # eating
    if snake.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        newsegment = Turtle()
        newsegment.speed(0)
        newsegment.shape('square')
        newsegment.color('blue')
        newsegment.penup()
        segments.append(newsegment)
        score = score + 1
        print(score)

    # move segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto((x,y))

    # move segment 0
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()
    time.sleep(0.1)
    win.mainloop()



