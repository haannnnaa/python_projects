import pgzrun
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'
menu_background_list = ['city_1', 'city_2', 'city_3', 'city_4', 'city_5', 'city_6', 'city_7', 'city_8']
WIDTH = 1000
HEIGHT = 700
TITLE = 'cybercar'
road = Actor('road', (500, 400))
menu_background = Actor(random.choice(menu_background_list), (500, 400))
start_button = Actor('start', (500, 250))
exit_button = Actor('exit', (500, 400))
shop_button = Actor('shop', (900, 500))
settings_button = Actor('settings', (900, 600))
info_button = Actor('info', (100, 500))
more_games_button = Actor('more_games', (100, 600))
back_button = Actor('back', (83, 215))
player_car = Actor('player_car', (562, 100))
left_to_right_car = Actor('left_to_right_car', (100, 332))
right_to_left_car = Actor('right_to_left_car', (900, 466))
lamp_1 = Actor('lamp1', (399, 213))
lamp_2 = Actor('lamp2', (600, 585))
lamp_3 = Actor('lamp3', (315, 501))
lamp_4 = Actor('lamp4', (683, 298))
black_lamp_1 = Actor('black_lamp1', (500, 400))
black_lamp_2 = Actor('black_lamp2', (510, 400))
black_lamp_3 = Actor('black_lamp3', (513, 399))

player_car_speed = 5
game = False
game_over = False
score = 0

def update():
    global player_car_speed, score, game_over

    if game and game_over == False:

        if keyboard.up and player_car.y >= 75 :
            player_car.y -= player_car_speed
        if keyboard.down :
            player_car.y += player_car_speed
        if player_car.y >= 850 :
            score += 1
            player_car.y = -50

        left_to_right_car.x += 5
        if left_to_right_car.x >= 1100 :
            left_to_right_car.x = - 50

        right_to_left_car.x -= 7
        if right_to_left_car.x <= -200 :
            right_to_left_car.x = 1200

        if player_car.colliderect(left_to_right_car) or player_car.colliderect(right_to_left_car) :
            game_over = True
            




def draw():
    global menu, score
    def menu():
        menu_background.draw()
        start_button.draw()
        exit_button.draw()
        info_button.draw()
        more_games_button.draw()
        settings_button.draw()
        shop_button.draw()


    menu()

    if game :
        road.draw()
        back_button.draw()
        player_car.draw()
        left_to_right_car.draw()
        right_to_left_car.draw()
        lamp_1.draw()
        lamp_2.draw()
        lamp_3.draw()
        lamp_4.draw()
        black_lamp_1.draw()
        black_lamp_2.draw()
        black_lamp_3.draw()

        screen.draw.text(f'score : {score}', topleft = (750, 180), fontsize = 35, color = (165, 0, 89))

def on_mouse_down(pos, button):
    global game, game_over
    if button == mouse.LEFT and player_car.collidepoint(pos) and game_over == False and game :
        sounds.horn1.play()
    if button == mouse.LEFT and left_to_right_car.collidepoint(pos) and game_over == False and game :
        sounds.horn4.play()
    if button == mouse.LEFT and right_to_left_car.collidepoint(pos) and game_over == False and game :
        sounds.horn5.play()
    if button == mouse.LEFT and (lamp_1.collidepoint(pos) or lamp_2.collidepoint(pos) or lamp_3.collidepoint(pos) or lamp_4.collidepoint(pos)) and game_over == False and game :
        sounds.light.play()
    if button == mouse.LEFT and back_button.collidepoint(pos) and game :
        game = False
        menu_background.image = random.choice(menu_background_list)
        menu()
        
    if start_button.collidepoint(pos) :
        menu_background.image = random.choice(menu_background_list)
        player_car.y = 100
        left_to_right_car.x = 100
        right_to_left_car.x = 900
        game = True
        game_over = False

pgzrun.go()