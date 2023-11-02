import pgzrun
import os
import random
from pgzhelper import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1000
HEIGHT = 700
TITLE = 'GAME CENTER'
button_pos = 0, 0
#-------------------------- main menu --------------------------#
main_menu_background = Actor('main_menu_background', (500, 350))
game_center_logo = Actor('game_center_logo', (1050, 220))
games_button = Actor('games_button_idle', (500, 800))
info_button = Actor('info_button_idle', (110, 700))
shop_button = Actor('shop_button_idle', (890, 700))
exit_button = Actor('exit_button_idle', (735, 700))
setting_button = Actor('setting_button_idle', (265, 635))
main_menu_button = Actor('main_menu_button_idle', (500, 800))
pink_background = Actor('pink_background', (500, 350))
busy_street_pic = Actor('busy_street_pic', (100,100))
exit_panel = Actor('exit_panel', (500,350))
no_button = Actor('no_idle', (688, 422))
yes_button = Actor('yes_idle', (306, 422))
game_choosing = False
main_menu_exit = False

def button_out_of_screen():
    games_button.y = 800
    info_button.y = 800
    exit_button.y = 800
    shop_button.y = 800
    setting_button.y = 800
    game_center_logo.x = 1300

#---------------- common buttons Actor ----------------#
home_button = Actor('home_button_idle')
play_button = Actor('play_button_idle')
repeat_button = Actor('repeat_button_idle')
guide_button = Actor('guide_button_idle')
music_on_button = Actor('music_on_button_idle')
music_off_button = Actor('music_off_button_idle')
music = True

#--------------------- busy street game---------------------#
left_car_list = ['police_car', 'left_car']
busy_street_road = Actor('busy_street_road', (500, 400))
player_car = Actor('player_car_down', (562, 100))
left_car = Actor(random.choice(left_car_list), (100, 332))
right_car = Actor('right_car', (900, 466))
police_car = Actor('police_car')
lamp_1 = Actor('lamp1', (399, 213))
lamp_2 = Actor('lamp2', (600, 585))
lamp_3 = Actor('lamp3', (315, 501))
lamp_4 = Actor('lamp4', (683, 298))
black_lamp_1 = Actor('black_lamp1', (500, 400))
black_lamp_2 = Actor('black_lamp2', (510, 400))
black_lamp_3 = Actor('black_lamp3', (513, 399))
pink_score_button = Actor('pink_score_button_idle', (750, 100))
pink_game_over_panel = Actor('pink_game_over_panel', (500, 350))
pink_in_game_setting_button = Actor('pink_in_game_setting_idle', (900, 100))
pink_panel = Actor('pink_panel', (500,350))
busy_street_game = False
busy_street_game_over = False
pink_in_game_setting = False
right_car_speed = random.randint(2,15)
left_car_speed = random.randint(2,15)
players_car_speed = 5
busy_street_score = 0

def update():
    global busy_street_score, left_car_speed, right_car_speed, busy_street_game_over
    #----------main menu buttons----------#
    if game_center_logo.x != 510 and game_choosing == False and main_menu_exit == False:
        game_center_logo.x -= 5
    elif game_center_logo.x == 510 and game_choosing :
        game_center_logo.x = 1050

    if games_button.y != 605 and game_choosing == False and main_menu_exit == False:
        games_button.y -= 5
    elif games_button.y == 605 and game_choosing :
        games_button.y = 800
    if games_button.collidepoint(button_pos) :
        games_button.image = 'games_button_hover'
    else:
        games_button.image = 'games_button_idle'

    if info_button.y != 635 and game_choosing == False  and main_menu_exit == False:
        info_button.y -= 5
    elif info_button.y == 635 and game_choosing :
        info_button.y = 700
    if info_button.collidepoint(button_pos):
        info_button.image = 'info_button_hover'
    else:
        info_button.image = 'info_button_idle'

    if shop_button.y != 635 and game_choosing == False  and main_menu_exit == False:
        shop_button.y -= 5
    elif shop_button.y == 635 and game_choosing :
        shop_button.y = 700
    if shop_button.collidepoint(button_pos):
        shop_button.image = 'shop_button_hover'
    else:
        shop_button.image = 'shop_button_idle'

    if exit_button.y != 635 and game_choosing == False  and main_menu_exit == False:
        exit_button.y -= 5
    elif exit_button.y == 635 and game_choosing :
        exit_button.y = 700
    if exit_button.collidepoint(button_pos):
        exit_button.image = 'exit_button_hover'
    else:
        exit_button.image = 'exit_button_idle'

    if setting_button.y != 635 and game_choosing == False  and main_menu_exit == False:
        setting_button.y -= 5
    elif setting_button.y == 635 and game_choosing :
        setting_button.y = 700
    if setting_button.collidepoint(button_pos):
        setting_button.image = 'setting_button_hover'
    else:
        setting_button.image = 'setting_button_idle'

    if yes_button.collidepoint(button_pos):
        yes_button.image = 'yes_hover'
    else:
        yes_button.image = 'yes_idle'

    if no_button.collidepoint(button_pos):
        no_button.image = 'no_hover'
    else:
        no_button.image = 'no_idle'

    #----------game choosing buttons----------#
    if main_menu_button.y != 605 and game_choosing:
        main_menu_button.y -= 5
    elif main_menu_button.y == 605 and game_choosing == False:
        main_menu_button.y = 800
    if main_menu_button.collidepoint(button_pos):
        main_menu_button.image = 'main_menu_button_hover'
    else:
        main_menu_button.image = 'main_menu_button_idle'

    #------------- common buttons -------------#
    if home_button.collidepoint(button_pos):
        home_button.image = 'home_button_hover'
    else:
        home_button.image = 'home_button_idle'

    if repeat_button.collidepoint(button_pos):
        repeat_button.image = 'repeat_button_hover'
    else:
        repeat_button.image = 'repeat_button_idle'

    if play_button.collidepoint(button_pos):
        play_button.image = 'play_button_hover'
    else:
        play_button.image = 'play_button_idle'

    if guide_button.collidepoint(button_pos):
        guide_button.image = 'guide_button_hover'
    else:
        guide_button.image = 'guide_button_idle'

    ''' if music_button.collidepoint(button_pos) :
        if music_button.image == 'music_on_button_idle' :
            music_button.image = 'music_on_button_hover'
        else:
            music_button.image = 'music_on_button_idle'

        if music_button.image == 'music_off_button_idle':
            music_button.image = 'music_off_button_hover'
        else:
            music_button.image = 'music_off_button_idle'''



    #-------------- busy street game --------------#
    if busy_street_game and busy_street_game_over == False:
        if keyboard.up and player_car.y >= 75 :
            player_car.y -= players_car_speed
        if keyboard.down :
            player_car.y += players_car_speed
        if player_car.y >= 850 :
            busy_street_score += 1
            player_car.y = -80
        
        left_car.x += left_car_speed
        if left_car.x >= 1100 :
            left_car.x = -100
            left_car.image = random.choice(left_car_list)
            left_car_speed = random.randint(2,15)
            left_car.x += left_car_speed
        
        right_car.x -= right_car_speed
        if right_car.x <= -100 :
            right_car.x = 1100
            right_car_speed = random.randint(2,15)
            right_car.x += right_car_speed

        if player_car.colliderect(left_car) or player_car.colliderect(right_car) :
            busy_street_game_over = True

        if pink_score_button.collidepoint(button_pos):
            pink_score_button.image = 'pink_score_button_hover'
        else:
            pink_score_button.image = 'pink_score_button_idle'

        if pink_in_game_setting_button.collidepoint(button_pos):
            pink_in_game_setting_button.image = 'pink_in_game_setting_hover'
        else:
            pink_in_game_setting_button.image = 'pink_in_game_setting_idle'

        

    

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

    if main_menu_exit :
        exit_panel.draw()
        yes_button.draw()
        no_button.draw()

    # busy street
    if busy_street_game :
        busy_street_road.draw()
        player_car.draw()
        left_car.draw()
        right_car.draw()
        black_lamp_1.draw()
        black_lamp_2.draw()
        black_lamp_3.draw()
        lamp_1.draw()
        lamp_2.draw()
        lamp_3.draw()
        lamp_4.draw()
        pink_score_button.draw()
        pink_in_game_setting_button.draw()
        
        if pink_score_button.collidepoint(button_pos) and busy_street_game_over == False:
            screen.draw.text(f'{busy_street_score}', fontsize = 25, topleft = (745, 110))
        else:
            screen.draw.text(f'{busy_street_score}', fontsize = 35, topleft = (745, 105))

        if pink_in_game_setting :
            pink_panel.draw()
            home_button.pos = 648, 105
            home_button.draw()
            play_button.pos = 648, 410
            play_button.draw()
            guide_button.pos = 648, 258
            guide_button.draw()
            if music == False :
                music_off_button.pos = 631, 565
                music_off_button.draw()
            if music :
                music_on_button.pos = 631, 565
                music_on_button.draw()
            if music == False :
                music_off_button.pos = 631, 565
                music_off_button.draw()
            if music :
                music_on_button.pos = 631, 565
                music_on_button.draw()
            

        if busy_street_game_over and pink_in_game_setting == False:
            pink_game_over_panel.draw()
            screen.draw.text(f'{busy_street_score}', fontsize = 100, topleft = (600, 280))
            repeat_button.pos = 354, 499
            repeat_button.draw()
            home_button.pos = 606, 499
            home_button.draw()

        

        
def on_mouse_move(pos):
    global button_pos
    button_pos = pos

def on_mouse_down(pos, button):
    global game_choosing, busy_street_game, busy_street_game_over, main_menu_exit, busy_street_score, pink_in_game_setting, music

    #-----------------menu-----------------#
    if exit_button.collidepoint(pos):
        main_menu_exit = True
        button_out_of_screen()
    if no_button.collidepoint(pos):
        main_menu_exit = False
    if yes_button.collidepoint(pos):
        quit()

    if games_button.collidepoint(pos):
        game_choosing = True
    
    if main_menu_button.collidepoint(pos):
        game_choosing = False
        main_menu()
    if busy_street_pic.collidepoint(pos) and game_choosing:
        sounds.busy_street_start.play()
        busy_street_game = True
        busy_street_game_over = False
        game_choosing = False

    #--------- busy street ---------#
    if button == mouse.LEFT and player_car.collidepoint(pos) and busy_street_game_over == False and busy_street_game:
        sounds.horn1.play()
    if button == mouse.LEFT and left_car.collidepoint(pos) and busy_street_game_over == False and busy_street_game:
        sounds.horn2.play()
    if button == mouse.LEFT and right_car.collidepoint(pos) and busy_street_game_over == False and busy_street_game:
        sounds.horn3.play()
    if button == mouse.LEFT and (lamp_1.collidepoint(pos) or lamp_2.collidepoint(pos) or lamp_3.collidepoint(pos) or lamp_4.collidepoint(pos)) and busy_street_game_over == False and busy_street_game :
        sounds.light_flicker.play()
    if button == mouse.LEFT and home_button.collidepoint(pos) and busy_street_game:
        if pink_in_game_setting:
            pink_in_game_setting = False
        busy_street_game = False
        busy_street_game_over = False
        busy_street_score = 0
        player_car.pos = 562, 100
        right_car.pos = 900, 466
        left_car.pos = 100, 332
        main_menu()
    if button == mouse.LEFT and repeat_button.collidepoint(pos) and busy_street_game_over and busy_street_game :
        busy_street_game_over = False
        busy_street_score = 0
        player_car.pos = 562, 100
        right_car.pos = 900, 466
        left_car.pos = 100, 332
    if button == mouse.LEFT and pink_in_game_setting_button.collidepoint(pos) and busy_street_game_over == False and busy_street_game :
        pink_in_game_setting = True
        busy_street_game_over = True
    if button == mouse.LEFT and play_button.collidepoint(pos) and busy_street_game :
        pink_in_game_setting = False
        busy_street_game_over = False

    if button == mouse.LEFT and music_on_button.collidepoint(pos):
        music = False
    if  button == mouse.LEFT and music_off_button.collidepoint(pos):
        music = True


def on_key_down(key):
    if key == keys.SPACE and busy_street_game_over == False and busy_street_game:
        sounds.horn4.play()
pgzrun.go()