import pygame
pygame.init()

# basic window
Width,Height = 800,600
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption(" Basic player movement")

# basic player
player_size = 50
player_x = Width//2
player_y = Height//2
speed = 50


running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -=speed # player_x-=5
    if keys[pygame.K_RIGHT]:
        player_x +=speed
    if keys[pygame.K_UP]:
        player_y -=speed
    if keys[pygame.K_DOWN]:
        player_y +=speed

    screen.fill((30,30,30))
    pygame.draw.rect(screen,(0,200,250),(player_x,player_y,player_size,player_size))
    pygame.display.update()

pygame.quit()
