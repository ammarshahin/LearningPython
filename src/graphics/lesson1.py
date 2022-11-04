import turtle


wn = turtle.Screen()
wn.title("My first window")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Game main Func
def main():
    while (True):
        wn.update()


main()
