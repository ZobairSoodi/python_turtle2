import turtle

s = turtle.getscreen()
turtle.hideturtle()
t = turtle.Turtle(shape="turtle")
t.color("black")
t.speed(11)
t.pensize(2)
list_color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def flag():
    t.color("green")
    t.pensize(5)
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.penup()
    t.forward(250)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.color("red")
    t.pendown()
    for i in range(2):
        t.forward(350)
        t.left(90)
        t.forward(200)
        t.left(90)


# flag()


def rectangle(fd, ran):
    for i in range(ran):
        t.color(list_color[i % 7])
        fd += 1
        t.forward(fd)
        t.left(50)


# rectangle(5, 200)


def circle():
    for i in range(40):
        t.color(list_color[i % 7])
        for j in range(4):
            t.fd(50)
            t.rt(90)
        t.rt(10)


# circle()


def flower(color, shape, has_circle):
    for i in range(12):
        t.color(color)
        t.begin_fill()
        t.circle(200, shape)
        t.left(120)
        t.circle(200, shape)
        t.left(180)
        t.end_fill()
    if has_circle is True:
        t.color("black")
        t.right(90)
        t.begin_fill()
        t.circle(shape/2)
        t.end_fill()
    """
    t.color("black")
    t.begin_fill()
    t.left(90)
    t.circle(200)
    t.end_fill()
    """


# flower("orange", 70, True)


def bruh():
    t.left(90)
    t.forward(90)
    t.circle(30, 90)
    t.left(90)
    t.forward(10)
    t.back(10)
    t.right(90)
    t.circle(30, 90)
    t.left(90)
    t.forward(60)
    t.back(60)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.circle(40, 180)
    t.forward(60)
    t.circle(40, 180)


turtle.done()
