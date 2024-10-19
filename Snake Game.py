import random
import pygame

# Initialize Pygame
pygame.init()

width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Indu Snake Game")


background_color = (150, 150, 150)
snake_color = (255, 255, 102)
food_color = (0, 0, 128)

snake_x, snake_y = width // 2, height // 2
change_x, change_y = 10, 0  

food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10


clock = pygame.time.Clock()

snake_body = [(snake_x, snake_y)]
snake_size = 10


def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y

    snake_x += change_x
    snake_y += change_y

    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        print("GAME OVER: Snake touched the boundary!")
        pygame.quit()
        quit()

   
    if (snake_x, snake_y) in snake_body[1:]:
        print("GAME OVER: Snake collided with itself!")
        pygame.quit()
        quit()

    # Add the new position to the snake's body
    snake_body.append((snake_x, snake_y))

    
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10
    else:
       
        del snake_body[0]

    # Fill the screen background
    game_screen.fill(background_color)


    pygame.draw.circle(game_screen, food_color, (food_x, food_y), snake_size // 2)

   
    for (x, y) in snake_body:
        pygame.draw.circle(game_screen, snake_color, (x, y), snake_size // 2)

    pygame.display.update()

# Game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -snake_size
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = snake_size
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x = 0
                change_y = -snake_size
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x = 0
                change_y = snake_size

  
    display_snake_and_food()

    
    clock.tick(10)
