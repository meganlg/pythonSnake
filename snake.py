## Megan Gillen
## April 2022

import turtle, random

class Game:
    '''
    Purpose:
        A setup of a turtle window, creates a snake and food class, and runs a game loop that allows you to playy the game "snake"
    Instance variables:
        self.player: class - a snake class that creates the snake
        self.pellet: class - a food class that creates the food pellet
    Methods:
        gameloop: checks to see if the snake has left the bounds of the window, or if it collides with itself. If not, it continues to run the function
    '''
    def __init__(self):      # init function
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0,0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        self.player = Snake(315, 315, 'green')
        self.pellet = Food()
        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.listen()
        turtle.mainloop()


    def gameloop(self):         #loop through game, run snake class, terminate when rules are violated

        tempx = self.player.segments[-1].xcor()
        tempy = self.player.segments[-1].ycor()
        collide = False
        for i in range(len(self.player.segments)-1):
            segx = self.player.segments[i].xcor()
            segy = self.player.segments[i].ycor()
            if tempx == segx and tempy == segy:
                collide = True

        if tempx > 600 or tempy > 600 or tempx < 0 or tempy < 0 or collide == True:
            turtle.write('GAME OVER', move=False, align='left', font = ('Arial',50,'normal'))
        else:
            self.player.move(self.pellet)
            turtle.ontimer(self.gameloop, 200)

        turtle.update()



class Snake:
    '''
    Purpose:
        represents a snake - a list of turtle objects that follow one another
    Instance variables:
        self.x: initial x position of the snake that the programmer enters (in the Game class above, it is set to 315)
        self.y: initial y position of the snake that the programmer enters (in the Game class above, it is set to 315)
        self.vy: snake's current velocity (gets added to self.x)
        self.vx: snake's current velocity (gets added to self.y)
        self.color: color of the snake that the programmer enters (in the Game class above, it is set to green)
        self.segments: list of turtle objects - squares - that make up the snake
        self.foodx: x position of the food pellet
        self.foody: y position of the food pellet
    Methods:
        grow: appends a new tutle object to self.segments, growing the length of the snake
        move: if the snake lands on a food pellet, it calls the grow function. Else, the turtle objects (snake) move in a connected line
        go_down: the snake moves down
        go_up: the snake moves up
        go_right: the snake moves right
        go_left: the snake moves left
    '''
    def __init__(self, x, y, color):      # init function
        self.x = x
        self.y = y
        self.vx = 30
        self.vy = 0
        self.color = color
        self.segments = []
        self.grow()

    def grow(self):                     # add 1 square to (grow) snake
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape('square')
        head.shapesize(1.5, 1.5)
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)

    def move(self, pellet):             # move, if snake collides with (eats)food pellet, run grow()
        self.foodx = pellet.foodx
        self.foody = pellet.foody
        self.x += self.vx
        self.y += self.vy

        if self.x == self.foodx and self.y == self.foody:
            pellet.grow_food()
            self.grow()
        else:
            for i in range(0,len(self.segments)-1):
                self.segments[i].setpos(self.segments[i+1].xcor(), self.segments[i+1].ycor())
            self.segments[-1].setpos(self.x, self.y)

    def go_down(self):
        self.vx = 0
        self.vy = -30
    def go_up(self):
        self.vx = 0
        self.vy = 30
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_left(self):
        self.vx = -30
        self.vy = 0


class Food:
    '''
    Purpose:
        represents a food pellet (turtle object) in the game 'Snake'
    Instance variables:
        self.foodx: x position of the food pellet (self.pellet)
        self.foody: y position of the food pellet (self.pellet)
        self.pellet: turtle object (circle) that is the food pellet for the snake
    Methods:
        grow_food: moves the position of the food pellet if the snake eats it (runs into/collides with it)
    '''
    def __init__(self):             # init function
        self.foodx = 0
        self.foody = 0
        self.pellet = turtle.Turtle()
        self.pellet.speed(0)
        self.pellet.fillcolor('red')
        self.pellet.shape('circle')
        self.pellet.shapesize(1.5, 1.5)
        self.pellet.penup()
        self.grow_food()

    def grow_food(self):            # put food at a random place on the board
        self.foodx = 15 + 30*random.randint(0,19)
        self.foody = 15 + 30*random.randint(0,19)
        self.pellet.setpos(self.foodx, self.foody)




Game()      ## run game
