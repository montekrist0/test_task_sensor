from turtle import Turtle
SENSOR_INIT_COORDINATES = (42, 42)


class Sensor(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(16/20)
        self.color("black")
        self.penup()
        self.speed(0.1)
        self.y_increment = -1
        self.x_increment = 4

    def change_y_direction(self):
        self.y_increment *= -1

    def move_left(self):
        self.setheading(180)
        self.forward(self.x_increment)
        self.setheading(90)

    def go_to_init_position(self):
        self.goto(SENSOR_INIT_COORDINATES)

    def start_control(self):
        self.pendown()
        self.setheading(90)
        while int(self.xcor()) >= -42:
            self.forward(self.y_increment)
            self.stamp()
            if abs(self.ycor()) >= 42:
                if self.xcor() == -42:
                    break
                self.move_left()
                self.change_y_direction()


