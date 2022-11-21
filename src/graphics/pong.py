import turtle

wn = turtle.Screen()


def init():
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)


def main():
    while (True):
        wn.update()
        ball_update()


def ball_update():
    dx = 0.2
    dy = 0.2
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)


def create_paddle(x, y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")  # by default square = 20 * 20
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)
    return paddle


def create_ball():
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("circle")  # by default square = 20 * 20
    paddle.color("white")
    paddle.penup()
    paddle.goto(0, 0)
    return paddle


def paddle_a_move_up():
    y = paddle_a.ycor()
    y += 20
    if y < wn.window_height() / 2:
        paddle_a.sety(y)


def paddle_a_move_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -1 * wn.window_height() / 2:
        paddle_a.sety(y)


def paddle_b_move_up():
    y = paddle_b.ycor()
    y += 20
    if y < wn.window_height() / 2:
        paddle_b.sety(y)


def paddle_b_move_down():
    y = paddle_b.ycor()
    y -= 20
    if y > -1 * wn.window_height() / 2:
        paddle_b.sety(y)


init()
paddle_a = create_paddle(-350, 0)
paddle_b = create_paddle(350, 0)
ball = create_ball()

wn.listen()
wn.onkeypress(paddle_a_move_up, "w")
wn.onkeypress(paddle_a_move_down, "s")
wn.onkeypress(paddle_b_move_up, "Up")
wn.onkeypress(paddle_b_move_down, "Down")

main()
