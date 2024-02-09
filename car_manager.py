from turtle import Turtle
import random
COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.reset_speed()
    def create_car(self, heading):
        random_chance = random.randint(1,8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,3) 
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(heading)
            random_y = random.randint(-300, 300)
            if heading == 180:
                new_car.goto(400, random_y)
            elif heading ==0:
                new_car.goto(-400, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
        
    def reset_speed(self):
        self.car_speed = STARTING_MOVE_DISTANCE