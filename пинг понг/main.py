import turtle
import winsound


window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)   

paddle_one = turtle.Turtle()
paddle_one.speed(0)    
paddle_one.color("white")
paddle_one.shape("square")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)  
paddle_one.penup()
paddle_one.goto(-350, 0)    
wid_one = 5

paddle_two = turtle.Turtle()
paddle_two.speed(0)     
paddle_two.color("white")
paddle_two.shape("square")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)   
wid_two = 5

ball = turtle.Turtle()
ball.speed(0)     
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)    
ball.dx = 0.2  
ball.dy = -0.2

score_one = 0
score_two = 0

write_score = turtle.Turtle()
write_score.speed(0)
write_score.color("white")
write_score.penup()
write_score.hideturtle()
write_score.goto(0, 260)
write_score.write("Player One: 0        Player Two: 0", align="center", font=("Courier", 24, "normal"))


# movement of paddle
def paddle_one_up():
    y = paddle_one.ycor() 
    y += 50
    paddle_one.sety(y)


def paddle_one_down():
    y = paddle_one.ycor()
    y -= 50
    paddle_one.sety(y)


def paddle_two_up():
    y = paddle_two.ycor() 
    y += 50
    paddle_two.sety(y)


def paddle_two_down():
    y = paddle_two.ycor() 
    y -= 50
    paddle_two.sety(y)

window.listen()
window.onkeypress(paddle_one_up, 'w')
window.onkeypress(paddle_one_down, 's')
window.onkeypress(paddle_two_up, 'Up')
window.onkeypress(paddle_two_down, 'Down')

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390: 
        ball.goto(0, 0)
        ball.dx = -0.2
        if ball.dy > 0 : 
            ball.dy = 0.2
        else :
            ball.dy = -0.2
        score_one += 1
        write_score.clear()
        write_score.write("Player One: {}           Player Two: {}".format(score_one, score_two), align="center",
                          font=("Courier", 24, "normal"))
        
        if (wid_one != 1 and wid_two != 1) :
            wid_one -= 1
            wid_two += 1
            paddle_one.shapesize(stretch_wid=wid_one, stretch_len=1)
            paddle_two.shapesize(stretch_wid=wid_two, stretch_len=1)

    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx = 0.2
        if ball.dy > 0 : 
            ball.dy = 0.2
        else :
            ball.dy = -0.2
        score_two += 1
        write_score.clear()
        write_score.write("Player One: {}           Player Two: {}".format(score_one, score_two), align="center",
                          font=("Courier", 24, "normal"))
        if (wid_one != 1 and wid_two != 1) :
            wid_two -= 1
            wid_one += 1
            paddle_two.shapesize(stretch_wid=wid_two, stretch_len=1)
            paddle_one.shapesize(stretch_wid=wid_one, stretch_len=1)

    if (340 < ball.xcor() < 350) and (paddle_two.ycor() + 40 > ball.ycor() > paddle_two.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (-340 > ball.xcor() > -350) and (paddle_one.ycor() + 40 > ball.ycor() > paddle_one.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)