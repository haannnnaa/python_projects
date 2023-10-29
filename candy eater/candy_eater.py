import pgzrun
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1000
HEIGHT = 563
TITLE = 'candy eater'

background_list = ['background2', 'background3']
heart_1 = Actor('heart', (50, 40))
heart_2 = Actor('heart', (50, 60))
heart_3 = Actor('heart', (50, 80))
healthy_food_list = ['banana', 'apple', 'broccoli', 'garlic', 'onion_01', 'onion_02', 'onion_03']
unhealthy_food_list = ['doughnut', 'cookie', 'cupcake', 'flummery', 'ice_cream_bar_01', 'ice_cream_bar_02']
random_num_list = [-50, -60, -65, -70, -75]

menu_background = Actor(random.choice(background_list) , (500 , 281.5))
game_background = Actor('background1' , (500 , 281.5))
play_button = Actor('start_button' , (500 , 281.5))
unhealthy_food = Actor(random.choice(unhealthy_food_list), (random.randint(60, 950), -20))
healthy_food = Actor(random.choice(healthy_food_list),  (random.randint(60, 950), -20))
char = Actor('char_left' , (500 , 470))
game_over_screen = Actor('game_over', (500, 281.5))

game = False
game_over = False
char_speed = 4
food_speed = 2
heart = 3
score = 0

def update():
    global char, char_speed, score, food_speed, game_over, heart

    if game and game_over == False:
        #----------------food movement----------------#
        unhealthy_food.y += food_speed
        if unhealthy_food.y >= HEIGHT + 50 :
            unhealthy_food.y = random.randrange(-151, -41 , 10)
            unhealthy_food.image = random.choice(unhealthy_food_list)
            unhealthy_food.x = random.randrange(60 + 1, 950 + 1 , 2)

        healthy_food.y += food_speed
        if healthy_food.y >= HEIGHT + 50 :
            healthy_food.y = random.randrange(-150, -40 , 10)
            healthy_food.image = random.choice(healthy_food_list)
            healthy_food.x = random.randrange(60 + 1, 950 + 1 , 2)
        
        #------------character movement-------------#
        if keyboard.left and char.x >= WIDTH - 948 :
            char.x -= char_speed
            char.image = 'char_left'
        if keyboard.right and char.x <= WIDTH - 52 :
            char.x += char_speed
            char.image = 'char_right'

        #---------------score and level-up---------------#
        if char.colliderect(unhealthy_food):
            sounds.eating.play()
            score += 1 
            unhealthy_food.y = random.randrange(-151, -41 , 10)
            unhealthy_food.x = random.randrange(60 + 1, 950 + 1 , 2)
            unhealthy_food.image = random.choice(unhealthy_food_list)



        #---------------game over---------------#
        if char.colliderect(healthy_food) :
            sounds.ew.play()
            healthy_food.y = random.randrange(-150, -40 , 10)
            healthy_food.image = random.choice(healthy_food_list)
            healthy_food.x = random.randrange(60 + 1, 950 + 1 , 2)
            heart -= 1
            if heart == 0 :
                sounds.death.play()
                if char.image == 'char_left' :
                    char.image = 'dead_char_left'
                else :
                    char.image = 'dead_char_right'
                game_over = True
                char_speed = 0
                food_speed = 0
        

def draw():
    global menu

    def menu():
        menu_background.draw()
        play_button.draw()

    menu()

    if game :
        game_background.draw()
        screen.draw.text(f'health = {heart}', color = (249, 86, 86), fontsize = 37, topleft = (850 , 20))
        screen.draw.text(f'score = {score}', color = (249, 86, 86), fontsize = 40, topleft = (850 , 45))
        unhealthy_food.draw()
        healthy_food.draw()
        char.draw()

        #-----heart-----#
        if heart == 3 :
            heart_1.draw()
            heart_2.draw()
            heart_3.draw()
        elif heart == 2 :
            heart_1.draw()
            heart_2.draw()
        elif heart == 1 :
            heart_1.draw()
            
        if game_over :
            game_over_screen.draw()


def on_mouse_down(pos,button):
    global game, game_over
    if play_button.collidepoint(pos) :
        game_over = False
        game = True


pgzrun.go()