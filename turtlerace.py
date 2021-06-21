"""
Programmer: Laxmi Gurung
Project: Turtle Race
Date: 05/20/2021
"""
from turtle import *
from random import *
import turtle 
import time


#setting up the screen and the turtle
fun = turtle.Turtle()
window = turtle.Screen()
window.setup (width=1.0, height=1.0, startx=0, starty=0)
fun.shape("turtle")
fun.pensize(3)
fun.hideturtle()

def firstPage():
    turtle.color('blue')
    turtle.speed(5)
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.write("Welcome!", font=("Courier",50),align='center')
    turtle.right(90)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.write("Summer Turtle Race", font=("Courier",40),align='center')
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.write("2021", font=("Courier",30),align='center')
    turtle.hideturtle()
    
firstPage()
time.sleep(3)
turtle.clear()

def location():
    #decorating the background for the race
    window = turtle.Screen()
    window.bgcolor('paleturquoise')
    fun.pu()
    fun.goto(450,350)
    fun.pd()
    fun.right(90)
    fun.pensize(10)
    fun.fd(700)
    fun.pu()
    fun.left(90)
    fun.fd(60)
    fun.left(90)
    fun.pd()
    fun.fd(700)
    fun.pu()
    fun.goto(-120,420)
    fun.right(90)
    fun.pd()
    fun.write('TURTLE RACE', font=('Courier',35))
    fun.hideturtle()

location()
time.sleep(3)

def audiencePage():
    turtle.color('blue')
    turtle.speed(5)
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.write("TO ALL THE AUDIENCE, PLEASE TAKE SEAT ON YOUR TOP RIGHT!", font=("Courier",30,'italic'),align='center')
    turtle.hideturtle()
    
audiencePage()
time.sleep(3)
turtle.clear()
#Audience
guest1 = Turtle()
guest1.speed(0)
guest1.color('seagreen')
guest1.shape("turtle")
guest1.pu()
guest1.goto(-350,400)
guest1.right(60)
guest1.pd()


guest2 = Turtle()
guest2.speed(0)
guest2.color('blue')
guest2.shape("turtle")
guest2.pu()
guest2.goto(-400,400)
guest2.right(60)
guest2.pd()


guest3 = Turtle()
guest3.speed(0)
guest3.color('gold')
guest3.shape("turtle")
guest3.pu()
guest3.goto(-450,400)
guest3.right(60)
guest3.pd()


guest4 = Turtle()
guest4.speed(0)
guest4.color('rosybrown')
guest4.shape("turtle")
guest4.pu()
guest4.goto(-500,400)
guest4.right(60)
guest4.pd()


guest5 = Turtle()
guest5.speed(0)
guest5.color('olive')
guest5.shape("turtle")
guest5.pu()
guest5.goto(-550,400)
guest5.right(60)
guest5.pd()
guest5.write('  Audience',font=('Courier',25))

time.sleep(5)
#Welcoming the players
def secondPage():
    turtle.color('blue')
    turtle.speed(5)
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.write("HERE COMES OUR PLAYERS", font=("Courier",50,'italic'),align='center')
    turtle.hideturtle()
    
secondPage()
time.sleep(3)
turtle.clear()

#player1
player1 = Turtle()
player1.speed(0)
player1.color('darkorchid')
player1.shape("turtle")
player1.shapesize(2,2,2)
player1.pu()
player1.goto(-250,200)
player1.pd()

#player2
player2 = Turtle()
player2.speed(0)
player2.color('red')
player2.shape("turtle")
player2.shapesize(2,2,2)
player2.pu()
player2.goto(-250,50)
player2.pd()

#player3
player3 = Turtle()
player3.speed(0)
player3.color('brown')
player3.shape("turtle")
player3.shapesize(2,2,2)
player3.pu()
player3.goto(-250,-100)
player3.pd()


#player4
player4 = Turtle()
player4.speed(0)
player4.color('black')
player4.shape("turtle")
player4.shapesize(2,2,2)
player4.pu()
player4.goto(-250,-250)
player4.pd()


time.sleep(5)
def thirdPage():
    turtle.color('blue')
    turtle.speed(5)
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.write("START", font=("Courier",50,'italic'),align='center')
    turtle.hideturtle()
    
thirdPage()
time.sleep(1)
turtle.clear()

#Beginning the race
def race():
    while True:
        turtle = choice([player1,player2,player3,player4])#choice()returns a random player from the list
        turtle.forward(randint(1, 5))
        if turtle.xcor() > 450:#it checks if the player crossed the x-cordinate
            break#to stop the loop

    turtle.shapesize(3,3,3)
    turtle.color('mediumblue')
    turtle.write('      Winner!', font=('Courier',15))

race()
time.sleep(10)

