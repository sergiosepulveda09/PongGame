import turtle

class GameField:
    def __init__(self):
    
        self.scoreA = 0
        self.scoreB = 0
        #Field
        self.division = turtle.Turtle()
        self.division.color("white")
        self.division.goto(0,400)
        self.division.goto(0,-400)
        #Pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,260)
        self.pen.write("Player A: 0   |   Player B: 0", align = "center", font = ("Courier", 24, "normal"))

    def clear(self):
        self.pen.clear()
        return
    def updateScore(self):
        self.pen.write("Player A: {}   |   Player B: {}".format(self.scoreA, self.scoreB), align = "center", font = ("Courier", 24, "normal"))
        return

    def scoreUp(self, score):
        if score == "A":
            self.scoreA += 1
        if score == "B":
            self.scoreB += 1
