from turtle import Screen, Turtle
from Area import Area
from Sensor import Sensor


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Test Task")
area = Area()
screen.update()
screen.tracer(1)


sensor = Sensor()
screen.listen()
screen.onkey(sensor.start_control, "s")
screen.onkey(sensor.go_to_init_position, "i")
# sensor.start_control()

screen.exitonclick()
