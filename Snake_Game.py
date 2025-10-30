#simple snake game 

import turtle
import time
import random

delay = 0.3

#set up screen
window = turtle.Screen()
window.title("Snake game by Zach")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen updates


#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction = "up"

#functions
#moving
def move_up():
    head.direction = "up"


def move_down():
    head.direction = "down"


def move_right():
    head.direction = "right"
    

def move_left():
    head.direction = "left"

#keybinding
window.listen()

#for the arrow keys
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onkeypress(move_left, "Left")

#for wsad 
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")

#snake apples
#snake head
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []





def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


#main game loop
while True:
    window.update()
#check for collision with food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)

    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

        #move segment 0 to where the head is 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()

    time.sleep(delay)

window.mainloop()