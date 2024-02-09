import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player_collision_area = 20
speed = 0.1
screen = Screen()
screen.listen()
screen.setup(width=800, height=900)
screen.title("Turtle Crossing Road")
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()
screen.onkeypress(key="Up",fun=player.move)
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car.create_car(180)
    if score.level == 5:
        car.reset_speed()
    if score.level >= 5:
        car.create_car(0)
    car.move_car()
    # detect collision with car
    for c in car.all_cars:
        car_x, car_y = c.position()
        player_x, player_y = player.position()
        player_x_min = player_x - player_collision_area / 2
        player_x_max = player_x + player_collision_area / 2
        player_y_min = player_y - player_collision_area / 2
        player_y_max = player_y + player_collision_area / 2
        if (car_x - 25 < player_x_max and car_x + 25 > player_x_min) and \
        (car_y - 10 < player_y_max and car_y + 10 > player_y_min):
            print("Player collision")
            game_is_on = False
            score.game_over()
    # detect successful crossing
    if player.is_at_finish_line() == True:
        player.go_to_start()
        car.speed_up()
        score.update_score()


screen.exitonclick()