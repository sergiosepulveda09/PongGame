#Player
import turtle

class Player: 
    
    
    def __init__(self, side):
        self.player = turtle.Turtle()
        self.player.speed(0)
        self.player.shape("square")
        self.player.color("white")
        self.player.penup()
        self.player.shapesize(stretch_wid = 5, stretch_len = 1)
        if side == "left":
            self.player.goto(-350,0)
        if side == "right":
            self.player.goto(350,0)


    def playerUp(self):
        y = self.player.ycor()
        y += 20
        self.player.sety(y)
        
        return

    def playerDown(self):
        y = self.player.ycor()
        y -= 20
        self.player.sety(y)
        return

    def getYcor(self):
        return self.player.ycor()


    
