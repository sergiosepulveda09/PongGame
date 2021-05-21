from GameField import GameField
from Player import Player
from Ball import Ball
import turtle

#Window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)


#Score
scoreA = 0
scoreB = 0

#Player A 

playerA = Player("left")

#Player B 

playerB = Player("right")

#Ball 

ball = Ball()

#GameField

gameField = GameField()

#Keyboard
window.listen()
window.onkeypress(playerA.playerUp, "w")
window.onkeypress(playerA.playerDown, "s")
window.onkeypress(playerB.playerUp, "Up")
window.onkeypress(playerB.playerDown, "Down")

while True:
    window.update()
    ball.setX()
    ball.setY()


    #Border 
    if ball.getYcor() > 290:
        ball.moveY()

    if ball.getYcor() < -290:
        ball.moveY()
    if ball.getXcor() > 390: 
        ball.goToCenter()
        ball.moveX()
        gameField.scoreUp("A")
        gameField.clear()
        gameField.updateScore()

    if ball.getXcor() <- 390: 
        ball.goToCenter()
        ball.moveX()
        gameField.scoreUp("B")
        gameField.clear()
        gameField.updateScore()

    if ((ball.getXcor() > 340 and ball.getXcor() < 350) and (ball.getYcor() < playerB.getYcor() + 60 and ball.getYcor() > playerB.getYcor()- 60)):
        ball.moveX()

    if ((ball.getXcor() <- 340 and ball.getXcor() >- 350) and (ball.getYcor() < playerA.getYcor() + 60 and ball.getYcor() > playerA.getYcor() - 60)):
        ball.moveX()


    
        
