import pygame
import random
pygame.init()
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("Fruit Catcher Game")
clock = pygame.time.Clock()

# Colors
PURPLE = (75,0,130)
YELLOW = (255,255,0)
ORANGE = (255,127,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# constants 
object_size = (140, 140)  # Size of the fruit and bomb objects
bowl_speed = 15
fps = 60
fruit_points = 10
max_time = 60
win_score = 700

# --- LOAD ASSETS (IMAGES) ---

# function to load and scale images
def load_image(path,size):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, size)
    return image

# bowl intialization
bowl_width = 200 
bowl_height = 110
bowl_image = load_image("pics/bowl_transparent.png", (bowl_width, bowl_height))
bowl_rect = bowl_image.get_rect()
bowl_rect.x = WIDTH //2
bowl_rect.y = HEIGHT - bowl_height

# use the load_image function to load and scale the fruit and bomb images
pear_img = load_image("pics/pear.png", (140, 170))
apple_img = load_image("pics/apple.png", object_size)
banana_img = load_image("pics/banana.png", object_size)
watermelon_img = load_image("pics/watermelon.png", object_size)
coconut_img = load_image("pics/coconut.png", object_size)
bomb_img = load_image("pics/bomb.png", object_size)

# load background images and scale them to fit the screen
bg = load_image("backgrounds/fruit_ninja.png", (WIDTH, HEIGHT))
bg2 = load_image("backgrounds/fruit_ninja2.png", (WIDTH, HEIGHT))

# fonts and texts initializing
big_font = pygame.font.SysFont("comic sans", 180)
font = pygame.font.SysFont("comic sans", 70)
gameover = big_font.render(f'Game Over', True, WHITE)
win = big_font.render(f'You Win!', True, WHITE)
Welcome = big_font.render(f'Fruit Catcher', True, WHITE)
Start_text = font.render(f'START', True, WHITE)
Quit_text = font.render(f'QUIT', True, WHITE)
Restart_text = font.render(f'RESTART', True, WHITE)
combo_text = font.render(f'COMBO!', True, WHITE)
exit_button_text = font.render(f'X', True, BLACK)

# Menus 
button_width = 1000
button_height = 200
button_gap = 80
button_center_x = WIDTH // 2
top_button_y = HEIGHT // 2 - button_height - button_gap // 2 + 50
bottom_button_y = top_button_y + button_height + button_gap

# Rect(x,y,width,height) - is an object
navbar = pygame.Rect(0, 0, WIDTH, 90)
play_btn = pygame.Rect(button_center_x - button_width // 2, top_button_y, button_width, button_height)
quit_btn = pygame.Rect(button_center_x - button_width // 2, bottom_button_y, button_width, button_height)
exit_btn = pygame.Rect(WIDTH-90,0,90,90)

# ----------------------------
#         FUNCTIONS
# ----------------------------

def menu(text):
    pygame.draw.rect(screen, BLUE, play_btn)
    pygame.draw.rect(screen, RED, quit_btn)
    screen.blit(text, (play_btn.centerx - text.get_width() // 2, play_btn.centery - text.get_height() // 2))
    screen.blit(Quit_text, (quit_btn.centerx - Quit_text.get_width() // 2, quit_btn.centery - Quit_text.get_height() // 2))
    pygame.display.flip()

def start_menu():
    screen.blit(Welcome,(WIDTH/2-Welcome.get_width()/2,50))
    menu(Start_text)

# spawn funcion to spawn fruits and bombs at random intervals
def spawn(fruit_list,image,rarity):
    if random.randint(1,rarity) == 1:
        new_fruit_rect = image.get_rect()
        new_fruit_rect.x = random.randint(0, WIDTH - new_fruit_rect.width)
        new_fruit_rect.y = -new_fruit_rect.height
        fruit_list.append(new_fruit_rect)

# move function to move fruits and bombs down the screen and delete them once they go off screen
def move(list):
    global score
    for item in list:
        item.y += current_speed
        if item.y > HEIGHT:
            list.remove(item)
            if list is not bombs:
                score -= 5

# function to check if the bowl has caught a fruit or bomb and update the score and lives accordingly
def catch(fruits,point):
    # use global to modify the global variables inside the function otherwise it will create a local variable with the same name
    global score, lives, slowmo, time_stamp, caught_fruits, time_stamp2
    hit_index = bowl_rect.collidelist(fruits)
    # if the hit_index is NOT -1 from collidelist, it means we have hit something
    if hit_index != -1:
        fruits.pop(hit_index) # Remove using the index
        score += point
        # add extra functionality for different groups of fruits and bombs
        if fruits is bombs:
            lives -= 1
        if fruits is bananas:
            slowmo = True
            time_stamp = time
        if fruits is apples:
            caught_fruits.append(1) # add the index of the apple we caught to the list of caught fruits
            time_stamp2 = time  


def reset_game():
    global pears, apples, bananas, watermelons, coconuts, bombs, caught_fruits
    global score, lives, base_fall_speed, time, time_stamp, time_stamp2, play
    global slowmo, combo, bowl_image

    pears = []
    apples = []
    bananas = []
    watermelons = []
    coconuts = []
    bombs = []
    caught_fruits = []
    score = 0
    lives = 3
    base_fall_speed = 4
    time = 0
    time_stamp = 0
    time_stamp2 = 0
    play = ''
    slowmo = False
    combo = False
    bowl_image = load_image("pics/bowl_transparent.png", (bowl_width, bowl_height))
    bowl_rect.x = WIDTH //2
    bowl_rect.y = HEIGHT - bowl_height

# set initial game state once
reset_game()

# ---------------------MAIN GAME LOOP ------------------------------>

running = True
while running:
    clock.tick(fps)
    if not(time >= max_time):
        time += 1/fps
    if slowmo:
        # slowmo speed will be half of normal speed
        current_speed = (base_fall_speed + (score // 70))/2
        screen.blit(bg2,(0,0))
    else:
        # Increase fall speed gradually over time based on score
        current_speed = base_fall_speed + (score // 70)
        screen.blit(bg,(0,0))

    # ---------------------------------------------------------
    # 1. EVENTS (mouse clicks and quit event)
    # ---------------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_mouse_pos = pygame.mouse.get_pos()
            if play_btn.collidepoint(current_mouse_pos):
                if play == '':
                    play = 'yes'
                if play == 'restart':
                    reset_game()
                    play = 'yes'
            if quit_btn.collidepoint(current_mouse_pos):
                if play != 'yes':
                    running = False
            if exit_btn.collidepoint(current_mouse_pos):
                if play != '':
                    running = False
    # ---------------------------------------------------------
    #                    2. GAME LOGIC   
    # ---------------------------------------------------------
    if play == '':
        start_menu()
    if play == 'yes':
        # Bowl movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bowl_rect.x -= bowl_speed
        if keys[pygame.K_RIGHT]:
            bowl_rect.x += bowl_speed

        # make sure the bowl stays within the screen boundaries
        if bowl_rect.left <= 0:
            bowl_rect.left = 0
        if bowl_rect.right >= WIDTH:
            bowl_rect.right = WIDTH

        # spawn each type of fruit with different spawn chances
        spawn(pears, pear_img, 80)
        spawn(apples, apple_img, 60)
        spawn(bananas, banana_img, 1000)
        spawn(watermelons, watermelon_img, 200)
        spawn(bombs, bomb_img, 150)
        spawn(coconuts, coconut_img, 200)
        # Move Fruits and bombs and delete them once off screen
        move(pears)
        move(apples)
        move(bananas)
        move(watermelons)
        move(coconuts)
        move(bombs)
        # collision detection and scoring
        catch(pears,fruit_points)
        catch(apples,fruit_points)
        catch(bananas,fruit_points*3)
        catch(watermelons,fruit_points)
        catch(coconuts,fruit_points)
        catch(bombs,-fruit_points*2)

        # slomo mode will last for 5 seconds after we catch the banana and will turn off
        if int(time) - int(time_stamp) >= 5:
            slowmo = False

        # we have a combo if the length of caught fruits is equal to 3 and less than 3 seconds have passed since catching those 3 fruits
        if len(caught_fruits) == 3 and int(time) - int(time_stamp2) <= 3:
            score += 10
            caught_fruits = [] # reset the caught fruits list so we can start counting again      
            combo = True

        # ---------------------------------------------------------
        # 5. DRAW EVERYTHING TO THE SCREEN
        # ---------------------------------------------------------
        # Draw Fruits and bomb
        for fruit in pears:
            screen.blit(pear_img, fruit)
        for fruit in apples:
            screen.blit(apple_img, fruit)
        for fruit in bananas:
            screen.blit(banana_img, fruit)
        for fruit in watermelons:
            screen.blit(watermelon_img, fruit)
        for fruit in coconuts:
            screen.blit(coconut_img, fruit)            
        for bomb in bombs:
            screen.blit(bomb_img, bomb)

        # draw navbar and exit button
        pygame.draw.rect(screen, RED, navbar)
        pygame.draw.rect(screen, RED, exit_btn,)
        pygame.draw.rect(screen, BLACK, exit_btn,2)
        screen.blit(exit_button_text, (exit_btn.x+20, exit_btn.y-10))

        # render text for dynmaic variables
        score_text = font.render(f"Score: {score:.0f}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        time_text = font.render(f"{time:.2f}", True, WHITE)

        screen.blit(score_text, (10, -15))
        screen.blit(lives_text, (WIDTH - lives_text.get_width()*1.5, -15))
        screen.blit(time_text, (WIDTH/2 - time_text.get_width()/2, -15))
        screen.blit(bowl_image, bowl_rect)

        # ---------------------------------------------------------
        # 6. Lives and special features
        # ---------------------------------------------------------

        # make the bowl wider the less lives we have
        if lives == 1:
            bowl_image = pygame.transform.scale(bowl_image, (bowl_width+50, bowl_height)) # width, height
        if lives == 2:
            bowl_image = pygame.transform.scale(bowl_image, (bowl_width+25, bowl_height)) # width, height

        # lose condition
        if (time >= max_time and score < win_score) or lives == 0:
            play = 'restart'
            screen.blit(gameover,(WIDTH/2-gameover.get_width()/2,50))
            menu(Restart_text)
        
        # win condition
        if score >= win_score and lives >= 1:
            play = 'restart'
            screen.blit(win,(WIDTH/2-win.get_width()/2,50))
            menu(Restart_text)

        if combo:
            screen.blit(combo_text, (bowl_rect.centerx - combo_text.get_width() // 2, bowl_rect.y - combo_text.get_height() - 10))
            # show combo text for 1 second only
            if int(time) - int(time_stamp2) >= 1:
                combo = False

        # show everything to display always
        pygame.display.flip()

pygame.quit()