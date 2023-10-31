import pgzrun
import os
import random
from pgzhelper import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1000
HEIGHT = 700
TITLE = 'GAME CENTER'

#--------------------------menu actors--------------------------#
main_menu_background = Actor('main_menu_background', (500, 350))
game_center_logo = Actor('game_center_logo', (1050, 220))
games_button = Actor('games_button', (500, 800))
info_button = Actor('info_button', (110, 700))
shop_button = Actor('shop_button', (890, 700))
exit_button = Actor('exit_button', (735, 700))
setting_button = Actor('setting_button', (265, 635))
main_menu_button = Actor('main_menu_button', (500, 800))
pink_background = Actor('pink_background', (500, 350))
busy_street_pic = Actor('busy_street_pic', (100,100))
game_choosing = False


#------------------busy street actors------------------#
busy_street_road = Actor('busy_street_road', (500, 400))
player_car = Actor('player_car_down', (562, 100))
car_right = Actor('car_right', (100, 332))
car_left = Actor('car_left', (900, 466))
police_car = Actor('police_car')
lamp_1 = Actor('lamp1', (399, 213))
lamp_2 = Actor('lamp2', (600, 585))
lamp_3 = Actor('lamp3', (315, 501))
lamp_4 = Actor('lamp4', (683, 298))
black_lamp_1 = Actor('black_lamp1', (500, 400))
black_lamp_2 = Actor('black_lamp2', (510, 400))
black_lamp_3 = Actor('black_lamp3', (513, 399))
busy_street_game = False
busy_street_game_over = False
players_car_speed = 2
busy_street_score = 0



def update():
    global busy_street_score
    #----------main menu buttons----------#
    if game_center_logo.x != 510 and game_choosing == False:
        game_center_logo.x -= 5
    elif game_center_logo.x == 510 and game_choosing :
        game_center_logo.x = 1050
    if games_button.y != 605 and game_choosing == False:
        games_button.y -= 5
    elif games_button.y == 605 and game_choosing :
        games_button.y = 800

    if info_button.y != 635 and game_choosing == False:
        info_button.y -= 5
    elif info_button.y == 635 and game_choosing :
        info_button.y = 700
    if shop_button.y != 635 and game_choosing == False:
        shop_button.y -= 5
    elif shop_button.y == 635 and game_choosing :
        shop_button.y = 700
    if exit_button.y != 635 and game_choosing == False:
        exit_button.y -= 5
    elif exit_button.y == 635 and game_choosing :
        exit_button.y = 700
    if setting_button.y != 635 and game_choosing == False:
        setting_button.y -= 5
    elif setting_button.y == 635 and game_choosing :
        setting_button.y = 700

    #----------game choosing buttons----------#
    if main_menu_button.y != 605 and game_choosing:
        main_menu_button.y -= 5
    elif main_menu_button.y == 605 and game_choosing == False:
        main_menu_button.y = 800

    if busy_street_game :
        if keyboard.up and player_car.y >= 75 :
            player_car.y -= players_car_speed
        if keyboard.down :
            player_car.y += players_car_speed
        if player_car.y >= 850 :
            busy_street_score += 1
            player_car.y = -80

def draw():
    global main_menu

    def main_menu():
        global game_center_logo
        main_menu_background.draw()
        game_center_logo.draw()
        games_button.draw()
        setting_button.draw()
        exit_button.draw()
        shop_button.draw()
        info_button.draw()


    main_menu()

    if game_choosing :
        pink_background.draw()
        main_menu_button.draw()
        busy_street_pic.draw()

    if busy_street_game :
        busy_street_road.draw()
        player_car.draw()
        car_right.draw()
        car_left.draw()
        black_lamp_1.draw()
        black_lamp_2.draw()
        black_lamp_3.draw()
        lamp_1.draw()
        lamp_2.draw()
        lamp_3.draw()
        lamp_4.draw()
        

def on_mouse_down(pos, button):
    global game_choosing, busy_street_game, busy_street_game_over

    if exit_button.collidepoint(pos):
        quit()

    if games_button.collidepoint(pos):
        game_choosing = True
    
    if main_menu_button.collidepoint(pos):
        game_choosing = False
        main_menu()
    if busy_street_pic.collidepoint(pos):
        busy_street_game = True
        busy_street_game_over = False
        game_choosing = False

    

pgzrun.go()