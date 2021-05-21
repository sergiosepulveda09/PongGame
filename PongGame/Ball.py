
import turtle

class Ball: 

    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx = 0.5
        self.ball.dy = 0.5

    def getYcor(self):
        return self.ball.ycor()

    def getXcor(self):
        return self.ball.xcor()

    def setX(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        return
    def setY(self):
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        return

    def moveX(self):
        self.ball.dx *= -1
        return

    def moveY(self):
        self.ball.dy *= -1
        return

    def goToCenter(self):
        self.ball.goto(0,0)
        return