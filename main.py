import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick
from solid import Solid

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255,255,255)
GREY = (105,105,105)
DARKGREEN = (0, 42, 0)
BLUE = (0,0,255)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREEN =(0,255,0)
LIGHTBLUE = (0,176,240)

score = 0
lives = 10

# Create a window
size = (960, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")

# List will contain all sprites
all_sprites_list = pygame.sprite.Group()

# Create paddle
paddle = Paddle(BLUE, 100, 10)
paddle.rect.x = 400
paddle.rect.y = 710

# Create ball
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 295

# Create bricks
all_bricks = pygame.sprite.Group()
for i in range(10):
    brick = Brick(RED,80,30)
    brick.rect.x = 17 + i* 94
    brick.rect.y = 53
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 17 + i* 94
    brick.rect.y = 97
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 17 + i* 94
    brick.rect.y = 141
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(GREEN,80,30)
    brick.rect.x = 17 + i* 94
    brick.rect.y = 185
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(LIGHTBLUE,80,30)
    brick.rect.x = 17 + i* 94
    brick.rect.y = 229
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add paddle and ball to sprites list
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# Loop will carry on until the user exits
carryOn = True

# Clock controls how fast the screen updates
clock = pygame.time.Clock()

# Main
while carryOn:
    # Main event loop
    for event in pygame.event.get(): # User did a thing
        if event.type == pygame.QUIT: # If user closes
              carryOn = False # Flag that we are done so we exit this loop

    # Moving the paddle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        paddle.moveRight(10)

    # Game logic
    all_sprites_list.update()

    # Check if the ball is bouncing against any walls
    if ball.rect.x>=947:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=3:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>710:
        ball.rect.x = 345
        ball.rect.y = 295
        pygame.time.wait(1000)
        lives -= 1
        if lives == 0:
            # Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (50,500))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the Game
            carryOn=False

    if ball.rect.y<41:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and paddle
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

    # Detect collisions between the ball and bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           # Display Level Complete for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (50,500))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the Game
            carryOn=False

    # Drawing code
    # Clear the screen to dark green
    screen.fill(DARKGREEN)

    # Draw boarder lines
    pygame.draw.line(screen, WHITE, [0, 38], [960, 38], 3)
    pygame.draw.line(screen, WHITE, [1, 38], [1, 720], 3)
    pygame.draw.line(screen, WHITE, [958, 38], [958, 720], 3)


    # Display the score and the number of lives
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (850,10))

    # Draws all the sprites at once
    all_sprites_list.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Once main program loop exited
pygame.quit()