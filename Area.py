from turtle import Turtle
INIT_COORDINATES = (-50, 50)


class Area(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.pen("red")
        self.speed("fastest")
        self.penup()
        self.goto(INIT_COORDINATES)
        self.create_area()

    def create_area(self):
        self.pendown()
        for _ in range(4):
            self.forward(100)
            self.right(90)
        self.penup()
        self.hideturtle()